from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from app.models import Contact

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email,
                          phone_no=phone_no, message=message)
        contact.save()
        messages.success(request, 'Submit Successful')
    return render(request, 'home.html')


def SignUp(request):
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect("signup")

        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=username,
            email=email,
            password=make_password(pass1)
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or  Password is incorrect!!!")
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect("login")
