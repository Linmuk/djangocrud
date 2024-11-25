from  django import forms
from  .models import Employee

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['first_name','last_name','employee_number','phone_number','image']