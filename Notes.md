# Notes and Helpful Bits

### Entering venv
```
source /home/kamivision/corsair/week-5/django-school-api-new/.school/bin/activate
```

### Resloved Permissions issue
`sudo chown -R kamivision:kamivision /home/kamivision/corsair/week-5/django-school-api-new/
`

- sudo runs the command with superuser privileges.
- chown changes the file owner and group.
- -R applies the change recursively to all files and subdirectories.
- kamivision:kamivision sets both the user and group owner to kamivision

### Migrate Model
`python manage.py makemigrations`
`python manage.py migrate`

### Enter Django Console
`python manage.py shell`

### Create App
`python manage.py startapp` + <app_name>

### Data transfer
 python manage.py dumpdata student_app.Student --indent 2 > student_app/fixtures/student_data.json