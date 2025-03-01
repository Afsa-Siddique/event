
from django.db import models
class tbl_admin(models.Model):
    password = models.CharField(max_length=200)
    email = models.EmailField()

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

from django.db import models

class EventPackage(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('luxury', 'Luxury'),
    ]

    name = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    max_guests = models.IntegerField()
    services = models.CharField(max_length=255)
    extra_services = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_name_display()} Package"

