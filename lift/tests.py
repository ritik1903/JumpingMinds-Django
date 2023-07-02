# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Lift

# # Create your tests here.

# NO_PARAMETER_ERROR = "No Parameters Passed"


# class CreateElevatorTestCase(APITestCase):
#     def test_creation(self):
#         response = self.client.get("/create/", {"count": "2"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["message"], "All Lifts created successfully")
#         self.assertEqual(response.data["Total_count"], 2)
#         self.assertEqual(response.data["Created_count"], 2)

#     def test_no_parameter_passed(self):
#         response = self.client.get("/create/")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, NO_PARAMETER_ERROR)


# class ListElevatorsTestCase(APITestCase):
#     def setUp(self):
#         Lift.objects.create()

#     def test_list_elevators(self):
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["id"], 1)
#         self.assertEqual(response.data[0]["current_floor"], 0)
#         self.assertEqual(response.data[0]["move_up"], False)
#         self.assertEqual(response.data[0]["door_open"], False)
#         self.assertEqual(response.data[0]["busy"], False)
#         self.assertEqual(response.data[0]["is_OOO"], False)


# class MoveElevatorsTestCase(APITestCase):
#     def setUp(self):
#         Lift.objects.create()

#     def test_move_lift_up(self):
#         response = self.client.get("/move/", {"floor": "6"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["current_floor"], 6)
#         self.assertEqual(response.data["move_up"], True)
#         self.assertEqual(response.data["id"], 1)

#     def test_move_lift_down(self):
#         pre_response = self.client.get("/move/", {"floor": "6"})
#         response = self.client.get("/move/", {"floor": "5"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["current_floor"], 5)
#         self.assertEqual(response.data["move_up"], False)
#         self.assertEqual(response.data["id"], 1)

#     def test_no_parameter_passed(self):
#         response = self.client.get("/move/")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, NO_PARAMETER_ERROR)


# class MarkElevatorOOOTestCase(APITestCase):
#     def setUp(self):
#         Lift.objects.create()
#         Lift.objects.create()

#     def test_lift_marked_OOO(self):
#         response = self.client.get("/ooo/", {"lift": "2"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], 2)
#         self.assertEqual(response.data["is_OOO"], True)

#     def test_lift_marked_back_active(self):
#         response = self.client.get("/ooo/", {"lift": "2"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], 2)
#         self.assertEqual(response.data["is_OOO"], False)

#     def test_lift_not_found(self):
#         response = self.client.get("/ooo/", {"lift": "4"})
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data, "Lift Not Found")

#     def test_no_parameter_passed(self):
#         response = self.client.get("/ooo/")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, NO_PARAMETER_ERROR)


# class ToggleElevatorDoorsTestCase(APITestCase):
#     def setup(self):
#         Lift.objects.create()

#     def test_elevator_door_closes(self):
#         response = self.client.get("/door/", {"lift": "1"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], 1)
#         self.assertEqual(response.data["door_open"], True)

#     def test_no_parameter_passed(self):
#         response = self.client.get("/door/")
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, NO_PARAMETER_ERROR)


# class HistoryPerLiftTestCase(APITestCase):
#     def setUp(self):
#         Lift.objects.create()

#     def test_history_of_lift_move_up(self):
#         self.client.get("/move/", {"floor": "6"})
#         response = self.client.get("/history/", {"lift": "1"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["Lift_id"], 1)
#         self.assertEqual(response.data["history"][0], "Lift Moved Up to floor 6")

#     def test_history_of_lift_move_Down(self):
#         self.client.get("/move/", {"floor": "-2"})
#         response = self.client.get("/history/", {"lift": "1"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["Lift_id"], 1)
#         self.assertEqual(response.data["history"][0], "Lift Moved Down to floor -2")
