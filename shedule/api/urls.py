from django.urls import path
from . import views

urlpatterns = [
    path('busroutes/', views.getRoutes, name="routes"),
    path('busroutes/<str:pk>/', views.getChild, name="busrout"),
    path('drivers/', views.getDrivers, name='drivers'),
]
