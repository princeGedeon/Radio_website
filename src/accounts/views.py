from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm


def connection(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,"Bienvenue")
            return redirect("home")
        else:
            messages.error(request,"Erreur d'authentification")
    return  render(request,"accounts/login.html")

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Votre compte a été créé')
            return redirect('login')
        else:
            messages.error(request,form.errors)
    return  render(request,"accounts/register.html",context={"form":form})

@login_required
def deconnection(request):
    logout(request)
    return redirect("login")