from django.db import models
from django.core import validators as val
from .validators import validate_name_format, validate_school_email, validate_combination_format


# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, 
        null = False, 
        blank = False,
        validators=[validate_name_format]
        )
    student_email = models.EmailField(
        null = False, 
        blank = False, 
        unique=True,
        validators=[validate_school_email]
        )
    personal_email = models.EmailField(
        null = False, 
        blank = False, 
        unique=True
        )
    locker_number = models.IntegerField(
        default=1, 
        null = False, 
        blank = False, 
        unique=True,
        validators=[
            val.MinValueValidator(1),
            val.MaxValueValidator(200)
        ]
        )
    locker_combination = models.CharField(
        max_length=255, 
        null = False, 
        blank = False, 
        default='12-12-12',
        validators=[validate_combination_format]
        )
    
    good_student = models.BooleanField(default=True)
    
    subjects = models.ManyToManyField(
        'subject_app.Subject',
        related_name='students'
    )
    
    def __str__(self):
        return f"< {self.name} - {self.student_email} - {self.locker_number}>"
    
    def add_subject(self, subject_id):
        if self.subjects.count() < 8:
            self.subjects.add(subject_id)
        else:
            raise Exception("This students class schedule is full!")
        
    def remove_subject(self, subject_id):
        if self.subjects.count() > 0:
            self.subjects.remove(subject_id)
        else:
            raise Exception("This students class schedule is empty!")
    
    def locker_assignment(self, new_locker):
        self.locker_number = new_locker
        #.save inserts or updates instance
        self.save()
    
    def student_status(self, status):
        self.good_student = status
        self.save()
            