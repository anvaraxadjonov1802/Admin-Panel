from django.shortcuts import render

def main(request):
    return render(
        request=request,
        template_name='index.html',
    )

def students(request):
    return render(
        request=request,
        template_name="students.html"
    )