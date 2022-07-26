from tkinter import ACTIVE
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .responseFormat import message_response
from .responseMessage import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TotalCountStudentSerializer
from .models import Student, TotalCountStudent
from .pagination import paginate
import datetime

# from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def studentList(request):
    students = Student.objects.filter(active=True)
    data = paginate(students, StudentSerializer, page=1, PAGE_SIZE=10)
    return Response(data)

@api_view(['GET'])
def studentDetail(request, pk):
    students = Student.objects.filter(id=pk)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def studentCreate(request):
    email = request.data.get('email',None)
    name = request.data.get('Name',None)

    count = get_object_or_404(TotalCountStudent, id=1)
    count.count=count.count+1

    year= datetime.datetime.now()
    year=str(year)[2:4]
    name=name.upper().split(" ",1)[0]
    # roll = f"{name.split(" ",1)[0]}/{year[:2]}/{str(count)}"
    roll = (name + "/" + year + "/" + str(count.count)) 
    if Student.objects.filter(email=email).exists():
        return Response(message_response(duplicate_entry), status = 400)
    else:
        count.save()
        data=request.data
        data['Roll']=roll
        serializer = StudentSerializer(data=data)
 
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance = student, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.active = False
    student.save()
    # student.delete()

    return Response('Student is deleted')




# class ListStudent(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class DetailStudent(generics.RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class CreateStudent(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class DeleteStudent(generics.DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


