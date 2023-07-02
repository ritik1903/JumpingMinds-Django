# from django.db import models

# # Create your models here.


# class Lift(models.Model):
#     current_floor = models.IntegerField(default=0)
#     move_up = models.BooleanField(default=False)
#     # if move up is false the lift moves down
#     door_open = models.BooleanField(default=False)
#     # if door open is false which means door is closed
#     busy = models.BooleanField(default=False)
#     is_OOO = models.BooleanField(default=False)


# class Requests_Per_Lift(models.Model):
#     lift = models.ForeignKey(Lift, on_delete=models.CASCADE)
#     history = models.CharField(max_length=200, default="called")
