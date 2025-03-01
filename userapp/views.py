

# Create your views here.
from rest_framework import generics

from adminapp.models import EventPackage
from vendor.models import Service, Vendor
from vendor.serializers import ServiceSerializer, VendorSerializer
from .serializers import EventPackageSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework import generics,viewsets
from .models import *
from .serializers import BookingSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from userapp.models import User
from userapp.serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from userapp.models import User
from userapp.serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from userapp.models import User
from userapp.serializers import UserSerializer
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Registration successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDestroyView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

        
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class EventPackageListCreateView(generics.ListCreateAPIView):
    queryset = EventPackage.objects.all()
    serializer_class = EventPackageSerializer
    http_method_names=['get']

class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({"services": serializer.data}, status=status.HTTP_200_OK)

from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user=User.objects.get(email=email,password=password)

        if user:
            return Response({
                "message": "Login successful",
                "user_id": user.id,
                "role":"user"
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
