from rest_framework import serializers
from adminapp.models import EventPackage
from vendor.models import Service
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone']

from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class EventPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPackage
        fields = '__all__'  

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'details', 'total_amount']
