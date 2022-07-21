from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student

# from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentDetail(request, pk):
    students = Student.objects.filter(id=pk)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

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
    student.delete()

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


