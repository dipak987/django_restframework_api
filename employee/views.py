from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here.
# create a user and to display
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# to retrive, update or delete a user by id
class EmployeeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer