from django.shortcuts import render, HttpResponse
from table.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email,
                          phone_no=phone_no, message=message)
        contact.save()
        messages.success(
            request, "Thank You For Contacting Us, we will get back soon!")
    return render(request, 'index.html')

