from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm



# Create your views here.
def show_view(request):
    employees=Employee.objects.all()
    return render(request,'testapp/index.html',{'employees':employees})
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'testapp/create.html',{'form':form, 'res':'true', 'msg':'Created sucessfully', 'classStyle':"alert alert-success"})
        else:
            return render(request,'testapp/create.html',{'form':form, 'res':'true', 'msg':'Something went wrong', 'classStyle':"alert alert-danger"})
    else:
        return render(request,'testapp/create.html',{'form':form})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    employees=Employee.objects.all()
    return render(request,'testapp/index.html',{'employees':employees, 'res':'true', 'msg':'Deleted successfully', 'classStyle':"alert alert-success"})
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST ,instance=employee)
        if form.is_valid():
            form.save()
            return render(request,'testapp/update.html',{'employee':employee,'res':'true','msg':'Updated sucessful', 'classStyle':"alert alert-success"})
        else:
            return render(request,'testapp/update.html',{'employee':employee,'res':'false', 'msg':'SOmething went wrong', 'classStyle':'alert alert-danger'})
    else:
        return render(request,'testapp/update.html',{'employee':employee,'res':'false'})
