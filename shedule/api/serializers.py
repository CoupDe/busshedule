from dataclasses import Field
from logging import exception
from unicodedata import category
from wsgiref.validate import validator
from django.forms import IntegerField
from rest_framework import serializers
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .models import Driver, RouteNumber


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'driver_category']


class RouteNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteNumber
        fields = ['num_route']
