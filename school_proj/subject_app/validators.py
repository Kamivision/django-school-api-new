from django.core.exceptions import ValidationError
import re

def validate_professor_name(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("Professor name must contain only letters and spaces.")
    
def validate_subject_name(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("Subject name must contain only letters and spaces.")