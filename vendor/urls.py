from django.urls import path
from .views import VendorListCreateView
from .views import *
from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    VendorListCreateView, 
    
    ServiceListCreateView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Vendor API",
        default_version="v1",
        description="API documentation for Vendor Management",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    # Vendor Endpoints
    path("vendors/registration/", VendorListCreateView.as_view(), name="vendor-list-create"),
    
    path('login/', VendorLoginView.as_view(), name='vendor-login'),
    path("services/", ServiceListCreateView.as_view(), name="service-list-create"),
    path('vendorshops/', VendoraddShopListCreateView.as_view(), name='vendor-shop-list-create'),
    path('vendorshops/<int:pk>/', VendoraddShopRetrieveUpdateDestroyView.as_view(), name='vendor-shop-detail'),
    # Swagger & Redoc Endpoints
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
