from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=14)
    employee_number=models.CharField(max_length=50,unique=True)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.employee_number}"