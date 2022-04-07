from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Driver
from .testdate import mydate
from .serializers import DriverSerializer


# Скорее всего сюда необходимо будет передавать список url CRUD
# Create your views here.


@api_view(['GET'])
def getDrivers(request):
    driver = Driver.objects.all()
    serializer = DriverSerializer(driver, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    return Response(mydate)


@api_view(['GET'])
def getChild(request, pk):
    children = mydate.objects.get(id=pk)
    return Response(children)
