from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average"]
        
    def get_students(self, stu):
        return stu.students.count()
        
    def get_grade_average(self, g):
        grades = g.grades.all()
        return round(sum([x.grade for x in grades])/len(grades),2)
        