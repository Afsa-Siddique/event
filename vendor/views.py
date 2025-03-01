from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import User
from userapp.serializers import UserSerializer
from .models import Vendor
from .serializers import VendorSerializer
from .serializers import *

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names=['post']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
             instance = serializer.save()
             return Response(
                {
                    "status": "success",
                    "message": "Vendor created successfully!",
                    "vendor_id": instance.id
                },
                status=status.HTTP_200_OK  # ✅ Force HTTP 200 OK
            )
        return Response(
            {
                "status": "error",
                "message": "Invalid data provided.",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST  # ✅ Handle bad requests explicitly
        )


from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from vendor.serializers import VendorSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    def post(self, request, *args, **kwargs):
        """Custom POST response for creating a new service"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Service created successfully","status":"success"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Failed to create service", "errors": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
from rest_framework.response import Response
from rest_framework import status

def get(self, request, *args, **kwargs):
    """Custom GET response for retrieving services"""
    services = self.get_queryset()
    serializer = self.get_serializer(services, many=True)
    
    # Return the list directly instead of wrapping it inside "data"
    return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
class VendorLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            vendor = Vendor.objects.get(email=email)

            # Validate password securely
            if password==vendor.password:
                serializer = VendorSerializer(vendor)
                return Response({"message": "Login successful","vendor_id": vendor.id, "Role":"Vendor"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

class VendoraddShopListCreateView(generics.ListCreateAPIView):
    queryset = VendoraddShop.objects.all()
    serializer_class = VendoraddShopSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vendor Shop added successfully!","status" :"success","data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendoraddShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendoraddShop.objects.all()
    serializer_class = VendoraddShopSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Vendor Shop deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)