from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .testdate import mydate

# Create your views here.
def getRoutes(request):
    return JsonResponse(mydate, safe=False)

