
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard,  name = "main" ),
    path('students/', students, name = "students")
]
