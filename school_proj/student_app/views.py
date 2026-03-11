from django.shortcuts import render
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
    
# class StudentView(APIView):
#     def get(self, request, name):
#         student = Student.objects.get(id=student_id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)