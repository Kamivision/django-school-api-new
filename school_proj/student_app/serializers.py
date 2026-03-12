from rest_framework import serializers
from subject_app.serializers import SubjectSerializer
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']
        
class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects",
        ]