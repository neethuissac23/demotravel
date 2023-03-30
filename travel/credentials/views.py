import datetime
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid User")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username Already Exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    password=password,
                    last_login=datetime.datetime.now(),
                    is_superuser=0,
                    username=uname,
                    first_name=fname,
                    last_name=sname,
                    email=email,
                    is_staff=1,
                    is_active=1,
                    date_joined=datetime.datetime.now()
                )
                user.save();
                messages.info(request, "User Created")
                return redirect('login')
        else:
            messages.info(request, "Password Not Matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
