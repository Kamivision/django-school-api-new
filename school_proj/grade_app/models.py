from django.db import models
from django.core import validators as val

# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=100,
        validators=[
            val.MinValueValidator(0.00),
            val.MaxValueValidator(100.00)]
        )
    a_subject = models.ForeignKey(
        'subject_app.Subject', 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='grades'
        )
    student = models.ForeignKey(
        'student_app.Student', 
        on_delete=models.SET_NULL,
        null=True, 
        related_name='grades'
    )