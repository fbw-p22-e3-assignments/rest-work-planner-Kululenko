from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, Shift
from .serializer import EmployeeSerializer, ShiftSerializer


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

