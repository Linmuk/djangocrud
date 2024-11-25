from django.shortcuts import render, get_object_or_404, redirect

from .forms import Employee_Form
from .models import Employee

# Create your views here.
def list_emp(request):
    employees=Employee.objects.all()
    return render(request, 'emp_list.html',{'employees':employees} )

def create_emp(request):
    if request.method=='POST':
        form = Employee_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employee_Form()
    return render(request,'create_emp.html',{'form':form})

def edit_emp(request, emp_id):
    employees = get_object_or_404(Employee, id=id)

    if request.method=='POST':
        form=Employee_Form(request.POST,request.FILES,instance=employees)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employee_Form(instance=employees)
    return render(request,'edit_emp.html',{'form':form})

def delete_emp(request,emp_id):
    employees=get_object_or_404(Employee,id=id)
    if request.method=='POST':
        employees.delete()
        return redirect('emp_list')
    return render(request,'cornfirm_delete.html',{'employees':employees})
