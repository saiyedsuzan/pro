# myapp/models.py

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # In a real-world app, use a password hashing library

class Student(models.Model):
    stu_id = models.CharField(max_length=50, unique=True)
    studentclass = models.IntegerField(choices=[(1, 'Class 1'), (2, 'Class 2')])
    password = models.CharField(max_length=256)  # Store the hashed password
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50,default="")
    dob=models.DateField(null=True)
    address=models.CharField(max_length=500,default="")
    # clas=models.CharField(max_length=3)
    # stu_id=models.CharField(max_length=10,primary_key=True,unique=True)
    # user_type=models.CharField(max_length=10,default='student')


    def __str__(self):
        return self.stu_id
