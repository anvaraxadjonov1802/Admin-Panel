
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard,  name = "dashboard" ),
    path('students/', students, name = "students"),
    path('teachers/', teachers, name = "teachers")
]
