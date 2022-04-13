from distutils.log import error
import string
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Driver, RouteNumber
from .customExceptions import RouteUniqExeption

from .serializers import DriverSerializer, RouteNumberSerializer


# Скорее всего сюда необходимо будет передавать список url CRUD
# Create your views here.


@api_view(['GET'])
def getDrivers(request):
    driver = Driver.objects.all()
    serializer = DriverSerializer(driver, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getRoutes(request):

    # print(**request.data)
    routes = RouteNumber.objects.all()

    # print(RouteNumber.objects.filter(num_route=request.data).exists())
    if request.method == 'GET':
        serializer = RouteNumberSerializer(routes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RouteNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Кривая реализация надо разбораться с валидаторами
        elif RouteNumber.objects.filter(num_route=request.data['num_route']).exists():
            return Response({'status': 403, 'message': 'Маршрут зарегистрирован в системе'})
        return Response({'status': 403, 'message': 'Введено некорректное значение'})

#


@api_view(['GET'])
def getChild(request, pk):
    children = mydate.objects.get(id=pk)
    return Response(children)
