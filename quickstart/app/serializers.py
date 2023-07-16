from app.models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    email=serializers.EmailField(max_length=200)
    password=serializers.CharField(max_length=200)
    phone=serializers.CharField(max_length=200)

    def create(self, validated_data):
        print('create method called')
        return Employee.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id=employee.id
        newEmployee.save() 
        return newEmployee


class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=200)
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    password=serializers.CharField(max_length=200) 

    def create(self, validated_data):
        print('create method called')
        return User.objects.create(**validated_data)