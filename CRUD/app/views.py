from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def Home(request):
    form = EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        form.save()
        form = EmployeeForm()
    data = Employee.objects.all()

    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html', context)

def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')

def Update_Record(request,id):
    if request.method=="POST":
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:    
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render(request,'update.html', context)