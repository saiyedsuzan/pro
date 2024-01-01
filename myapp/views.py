# myapp/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import TeacherRegistrationForm, StudentRegistrationForm, StudentLoginForm
from .models import Teacher, Student 

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'register_teacher.html', {'form': form})



def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return redirect('login_student')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            stu_id = form.cleaned_data['stu_id']
            password = form.cleaned_data['password']
            studentclass = form.cleaned_data['studentclass']
            try:
                student = Student.objects.get(stu_id=stu_id, studentclass=int(studentclass))
                if check_password(password, student.password):
                    if student.studentclass == 1:
                        return redirect('class1')
                    elif student.studentclass == 2:
                        return redirect('class2')
                    elif student.studentclass == 2:
                        return redirect('class2')
                    elif student.studentclass == 2:
                        return redirect('class2')
                    elif student.studentclass == 2:
                        return redirect('class2')
                    elif student.studentclass == 2:
                        return redirect('class2')
                    elif student.studentclass == 2:
                        return redirect('class2')

            except Student.DoesNotExist:
                pass
        return redirect('login')
    else:
        form = StudentLoginForm()
    return render(request, 'login_student.html', {'form': form})

def class1(request):
    return render(request, 'class1.html')

def class2(request):
    return render(request, 'class2.html')

        # Display the login form


    # if request.method == 'POST':
    #     form = StudentLoginForm(request.POST)
    #     if form.is_valid():
    #         stu_id = form.cleaned_data['stu_id']
    #         password = form.cleaned_data['password']
            
    #         # Authenticate student
    #         student = authenticate(request, stu_id=stu_id, password=password)
            
    #         if student is not None:
    #             # Log in the student
    #             login(request, student)
    #             return redirect('student_dashboard')  # Redirect to student dashboard upon successful login
    #         else:
    #             form = StudentLoginForm()
    #             return render(request, 'login_student.html', {'form': form})
    #     form = StudentLoginForm(data=request.POST)
    #     if form.is_valid():
    #         # Extract cleaned data
    #         stu_id = form.cleaned_data.get('stu_id')
    #         password = form.cleaned_data.get('password')
            
    #         # Custom authentication using stu_id
    #         student = authenticate(request=request, stu_id=stu_id, password=password)
            
    #         if student is not None:
    #             # Log in the student
    #             login(request, student)
    #             return redirect('student_dashboard')  # Redirect to student dashboard upon successful login
    #         else:
    #             # Display error if authentication fails
    #             messages.error(request, "Invalid student ID or password")
    #     else:
    #         # Display error if form is invalid
    #         messages.error(request, "Invalid form data")
    # else:
    #     # For GET requests or when form is not valid, initialize the form
    #     form = StudentLoginForm()

    # return render(request, 'login_student.html', {'form': form})
