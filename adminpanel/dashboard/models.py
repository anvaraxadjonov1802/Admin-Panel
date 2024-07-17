from django.db import models



class Phone_numbers(models.Model):
    phone_number = models.IntegerField()
    created_at = models.TimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return str(self.phone_number)
    

class Conditions(models.Model):
    condition = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return str(self.condition)
    
class Teachers(models.Model):
    name = models.CharField(max_length = 100)
    fname = models.CharField(max_length = 100)
    image = models.ImageField()
    phone_number = models.ForeignKey(Phone_numbers, on_delete=models.CASCADE, related_name='phone_number_of_teacher')
    created_at = models.TimeField(auto_now_add = True)
    
    @property
    def imageURL(self):
        return self.image.url
    
    def __str__(self) -> str:
        return str(self.name + " " + self.fname)
    
class Groups(models.Model):
    name = models.CharField(max_length = 200)
    teacher = models.ForeignKey(Teachers, on_delete = models.CASCADE, related_name = 'teacher_of_group')
    created_at = models.TimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return str(self.name)
    
    
class Students(models.Model):
    name = models.CharField(max_length = 100)
    fname = models.CharField(max_length = 100)
    image = models.ImageField()
    phone_number = models.ForeignKey(Phone_numbers, on_delete=models.CASCADE, related_name='phone_number_of_student')
    group = models.ForeignKey(Groups, on_delete = models.CASCADE, related_name = 'group_of_student')
    condition = models.ForeignKey(Conditions, on_delete = models.CASCADE, related_name = 'condition_of_student')
    created_at = models.DateField(auto_now_add = True)
    
    @property
    def imageURL(self):
        return self.image.url
    
    def __str__(self) -> str:
        return str(self.name + " " + self.fname)
    
class Payments(models.Model):
    sum = models.IntegerField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE,  related_name = 'student_of_payment')
    image = models.ImageField()
    created_at = models.TimeField(auto_now_add = True)
    
    @property
    def imageURL(self):
        return self.image.url
    
    def __str__(self) -> str:
        return str(self.sum)
    
class Debts(models.Model):
    sum = models.IntegerField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE,  related_name = 'student_of_debt')
    created_at = models.TimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return str(self.sum)
    
    
    

