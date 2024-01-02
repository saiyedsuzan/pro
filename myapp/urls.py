# myapp/urls.py

from django.urls import path
from .views import register_teacher, register_student, login_student,class1,class2,login_teacher

urlpatterns = [
    path('register_teacher', register_teacher, name='register_teacher'),
    path('', register_student, name='register_student'),
    path('login_student', login_student, name='login_student'),
    path('teacher_login', login_teacher, name='teacher_login'),
    # path('student_dashbord',student_dashbord, name='student_dashbord'),
    path('class1',class1, name='class1'),
    path('class2',class2, name='class2'),
    
    # Add other URLs as needed
]
