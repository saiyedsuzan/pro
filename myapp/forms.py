# myapp/forms.py

from django import forms
from .models import Teacher, Student

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['tec_id','first_name','last_name', 'email', 'password','subject_taught']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stu_id', 'studentclass', 'password','first_name','last_name','email','dob','address']
        widgets = {
            'password': forms.PasswordInput()
        }

class StudentLoginForm(forms.Form):
    stu_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    studentclass = forms.ChoiceField(choices=[(1, 'Class 1'), (2, 'Class 2')])

class TeacherLoginForm(forms.Form):
    tec_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
