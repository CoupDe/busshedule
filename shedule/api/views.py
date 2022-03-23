from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .testdate import mydate

# Скорее всего сюда необходимо будет передавать список url CRUD
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    return Response(mydate)


@api_view(['GET'])
def getChild(request, pk):
    children = None
    for i in (mydate):
        if i['id'] == pk:
            children = i
            break
    return Response(children)
