from django.shortcuts import render
from .models import *

def dashboard(request):
    students = Students.objects.all().order_by('-id')
    teachers = Teachers.objects.all().order_by('-id')
    groups = Groups.objects.all().order_by('-id')
    payments = Payments.objects.all().order_by('-id')
    
    st_count = 0
    tr_count = 0
    gr_count = 0
    sum = 0
    
    for i in payments:
        sum += int(i.summ)
    
    for i in students:
        st_count += 1
        
    for i in teachers:
        tr_count += 1
        
    for i in groups:
        gr_count += 1
        
    
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
    return render(
        request=request,
        template_name="students.html"
    )