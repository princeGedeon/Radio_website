from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm


def connection(request):
    return  render(request,"accounts/login.html")

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Votre compte a été créé')
            return redirect('login')
    return  render(request,"accounts/register.html",context={"form":form})

def deconnection(request):
    pass