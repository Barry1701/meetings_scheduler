from datetime import time
from django.db import models

# Create your models here.




class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField(default=0)
    room_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} : Room{self.room_number} On Floor {self.floor}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_date = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} at {self.start_date} on {self.date}'




