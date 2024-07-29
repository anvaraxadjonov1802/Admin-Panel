from django.shortcuts import render,redirect
from .models import *
from .form import PaymentsForm
from django.http import HttpResponse


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
    
def payments(request):
    payments = Payments.objects.all().order_by('-id')
    students = Students.objects.all().order_by('-id')
    
    context = {
        "payments" : payments,
        "students" : students
    }
    return render(
        context=context,
        request=request,
        template_name="payments.html" 
    )
def groups(request):
    groups = Groups.objects.all().order_by("-id")
    students = Students.objects.all()
    main_list = []
    count = 0
    item = []
    for i in groups:
        item.append(f"{i.name}")
        for j in students:
            if j.group.name == i.name:
                count += 1
        item.append(count)
        main_list.append(item)
        item = []
        
    
    context = {
        "groups" : groups,
        "count" : main_list
    }
    
    return render(
        context=context,
        template_name="groups.html",
        request=request
    )
    
def image_view(request, id):
    payments = Payments.objects.filter()
    for i in payments:
        if id == i.id:
            payment = i
            
    context = {
        "payment" : payment
    }
    return render(
        request=request,
        template_name="kvitansiya.html",
        context=context
    )

def payment_input(request):
    
    students = Students.objects.all()
    if request.method == 'POST':
        sum = request.POST.get('sum')
        student = request.POST.get('student')
        img = request.POST.get('img')
        
        form = PaymentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'payments_input.html', {'form': form, 'img_obj': img_obj})
        print(sum)
        print(student)
        print(form)
        # payment = Payments.objects.create(
        #     sum = sum,
        #     student = student,
        #     image = img
        # )
        # payment.save()
        return redirect('dashboard')
    
    context = {
        "students" : students
    }
    return render(
        request=request,
        template_name='payment_input.html',
        context=context
    )

def group_input(request):
    
    teachers = Teachers.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        
        
        print(name)
        for i in teachers:
            if i.id == int(teacher):
                teacher = i
        # print(teacher)
                
        group = Groups.objects.create(
            name =  name,
            teacher = teacher   
        )
        group.save()
        return redirect('groups')
    
    context = {
        "teachers" : teachers
    }
    return render(
        request=request,
        template_name='groups_input.html',
        context=context
    )
    
