from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AllSubjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
class SubjectView(APIView):
    def get(self, request, name):
        subject = Subject.objects.get(subject_name=name.title())
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)