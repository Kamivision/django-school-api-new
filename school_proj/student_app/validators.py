from django.core.exceptions import ValidationError
import re


# validate_name_format: Only accepts string in the following format "First M. Last"
# Validation Error: 'Name must be in the format "First Middle Initial. Last"'
def validate_name_format(value:str):
    if not re.match("^[A-Z][a-z]+ [A-Z]. [A-Z][a-z]+$", value):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')

# validate_school_email: Only accepts string ending with "@school.com"
# Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
def validate_school_email(email):
    if not re.match(r'^[\w\.-]+@school\.com$', email):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')
    

# validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
# Validation Error: 'Combination must be in the format "12-12-12"'
def validate_combination_format(combo):
    if not re.match("^\d{1,2}-\d{1,2}-\d{1,2}", combo):
        raise ValidationError('Combination must be in the format "12-12-12"')