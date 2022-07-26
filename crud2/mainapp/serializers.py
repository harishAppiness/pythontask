from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TotalCountStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalCountStudent
        fields = '__all__'


