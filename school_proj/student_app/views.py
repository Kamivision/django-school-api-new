from django.shortcuts import render, get_object_or_404
from .serializers import StudentSerializer, StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

# Create your views here.
class AllStudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentAllSerializer(students, many=True)
        return Response(serializer.data)
    
class StudentView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)