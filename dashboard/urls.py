
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard,  name = "dashboard" ),
    path('students/', students, name = "students"),
    path('teachers/', teachers, name = "teachers"),
    path('payments/', payments, name = "payments"),
    path('groups/', groups, name="groups"),
    path('<int:id>', image_view, name="image_view"),
    path('payment_input', payment_input, name="payment_input"),
    path("group_add/", group_input, name="group_add")
]
