from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Lift, Requests_Per_Lift
from .serializer import LiftSerializer


def choose_lift(requiredFloor):
    lifts = Lift.objects.all()
    distance = 50000
    closest_lift = 1
    for lift in lifts:
        if lift.is_OOO:
            continue
        else:
            if abs(requiredFloor - lift.current_floor) < distance:
                distance = abs(requiredFloor - lift.current_floor)
                closest_lift = lift.id
    return closest_lift


NO_PARAMETER_ERROR = "No Parameters Passed"


class LiftViewSet(viewsets.ModelViewSet):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer

    @action(methods=["GET"], url_path="create", detail=False)
    def create_elevators(self, request):
        try:
            count = int(request.query_params["count"])
            bulk = []
            for _ in range(count):
                bulk.append(Lift())
            Lift.objects.bulk_create(bulk)
            data = {
                "message": "All Lifts created successfully",
                "Total_count": self.queryset.count(),
                "Created_count": count,
            }
            for lift in self.queryset:
                Requests_Per_Lift.objects.create(lift=lift, history="Lift Created")
            print(data)
            return Response(data)
        except Exception:
            return Response(exception=True, data=NO_PARAMETER_ERROR, status=400)

    @action(methods=["GET"], url_path="move", detail=False)
    def move_elevator(self, request):
        try:
            floor = int(request.query_params["floor"])
            LiftId = choose_lift(floor)
            lift = Lift.objects.get(id=LiftId)
            move_up = False
            if lift.current_floor < floor:
                move_up = True
            lift.move_up = move_up
            lift.current_floor = floor
            lift.save()
            if move_up:
                Requests_Per_Lift.objects.create(
                    lift=lift, history="Lift Moved Up to floor " + str(floor)
                )
            else:
                Requests_Per_Lift.objects.create(
                    lift=lift, history="Lift Moved Down to floor " + str(floor)
                )
            return Response(LiftSerializer(lift).data)

        except Exception:
            return Response(exception=True, status=400, data=NO_PARAMETER_ERROR)

    @action(methods=["GET"], url_path="ooo", detail=False)
    def mark_ooo(self, request):
        try:
            lift_number = int(request.query_params["lift"]) - 1
            if lift_number >= 0 and lift_number < len(self.queryset):
                lift = self.queryset[lift_number]
                lift.is_OOO = not lift.is_OOO
                lift.save()
                if lift.is_OOO:
                    Requests_Per_Lift.objects.create(
                        lift=lift, history="Lift Marked in Maintenance"
                    )
                else:
                    Requests_Per_Lift.objects.create(
                        lift=lift, history="Lift Marked active"
                    )
                return Response(LiftSerializer(lift).data)
            return Response(status=404, data="Lift Not Found")
        except Exception:
            return Response(exception=True, data=NO_PARAMETER_ERROR, status=400)

    @action(methods=["GET"], url_path="door", detail=False)
    def toggle_door(self, request):
        try:
            lift_number = int(request.query_params["lift"]) - 1
            if lift_number >= 0 and lift_number < len(self.queryset):
                lift = self.queryset[lift_number]
                lift.door_open = not lift.door_open
                lift.save()
                if lift.door_open:
                    Requests_Per_Lift.objects.create(
                        lift=lift, history="Lift Door Opened"
                    )
                else:
                    Requests_Per_Lift.objects.create(
                        lift=lift, history="Lift Door Closed"
                    )
                return Response(LiftSerializer(lift).data)
            return Response(status=404, data="Lift not found")
        except Exception:
            return Response(status=400, data=NO_PARAMETER_ERROR)

    @action(methods=["GET"], url_path="history", detail=False)
    def history_per_lift(self, request):
        try:
            lift_number = int(request.query_params["lift"]) - 1
            print(lift_number)
            if lift_number >= 0 and lift_number < len(self.queryset):
                lift = self.queryset[lift_number]
                history_per_lift = Requests_Per_Lift.objects.filter(lift=lift)
                lift_history = []
                for history in history_per_lift:
                    lift_history.append(history.history)
                return Response({"Lift_id": lift.id, "history": lift_history})
            else:
                return Response(status=404, data="Lift not found")
        except Exception:
            return Response(
                exception=True, data="Please Provide a lift number", status=400
            )
