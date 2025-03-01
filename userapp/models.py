from django.db import models
from adminapp.models import *

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)  
   
    def __str__(self):
        return self.name

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    date_of_marriage = models.DateField()
    number_of_participants = models.PositiveIntegerField()
    event_package = models.ForeignKey(EventPackage, on_delete=models.CASCADE, related_name="bookings")  

    def __str__(self):
        return f"{self.name} - {self.date_of_marriage} ({self.event_package.name})"
