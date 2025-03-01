from rest_framework import serializers
from .models import Vendor
from .models import *
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class VendoraddShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendoraddShop
        fields = '__all__' 