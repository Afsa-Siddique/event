from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import EventPackageListCreateView, UserListCreateView, UserRetrieveUpdateDestroyView
from .views import *
# Router

schema_view = get_schema_view(
    openapi.Info(
        title="Event API",
        default_version="v1",
        description="API documentation for the event app.",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

urlpatterns = [
   re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),


    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
     path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('login/', LoginView.as_view(), name='login'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path("packages/", EventPackageListCreateView.as_view(), name="list_create_packages"),
     path('userviewservices/', ServiceListView.as_view(), name='user-view-services'),


    path('', include(router.urls)),
]
