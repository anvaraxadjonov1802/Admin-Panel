from django.shortcuts import render
from .models import *

def dashboard(request):
    all_students = Students.objects.all().order_by('-id')
    teachers = Teachers.objects.all().order_by('-id')
    groups = Groups.objects.all().order_by('-id')
    payments = Payments.objects.all().order_by('-id')
    
    st_count = 0
    tr_count = 0
    gr_count = 0
    sum = 0
    
    for i in payments:
        sum += int(i.sum)
    
    for i in all_students:
        st_count += 1
        
    for i in teachers:
        tr_count += 1
        
    for i in groups:
        gr_count += 1
        
    students = []
    hisob = 6
    for i in all_students:
        if hisob > 0:
            students.append(i)
            hisob-=1
    
    
    context = {
        "students" : students,
        'teachers' : teachers,
        "students_count" : st_count,
        "teachers_count" : tr_count,
        "groups_count" : gr_count,
        "payment_sum" : sum
    }
    return render(
        context=context,
        request=request,
        template_name='index.html',
    )

def students(request):
    students = Students.objects.all().order_by('-id')
    context = {
        "students" : students,
    }
    return render(
        context=context,
        request=request,
        template_name="students.html" 
    )
    
def teachers(request):
    teachers = Teachers.objects.all().order_by('-id')
    context = {
        "teachers" : teachers,
    }
    return render(
        context=context,
        request=request,
        template_name="teachers.html" 
    )