from django.urls import path
from . import views

urlpatterns = [
    path('busroutes/<str:pk>/', views.getChild, name="busrout"),
    path('busroutes/', views.getRoutes, name="busroutes"),
    path('drivers/', views.getDrivers, name='drivers'),
]
