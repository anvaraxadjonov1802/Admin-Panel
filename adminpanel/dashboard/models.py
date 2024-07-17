from django.db import models



class Phone_numbers(models.Model):
    phone_number = models.IntegerField()
class Students(models.Model):
    name = models.CharField(max_length = 100)
    fname = models.CharField(max_length = 100)
    phone_number = models.ForeignKey()
    created_at = models.TimeField(auto_now_add = True)
