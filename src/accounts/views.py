from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

# Create your views here.
from Post_app.models import Video
from accounts.forms import UserForm
from accounts.models import User


def connection(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,"Bienvenue")
            if user.is_completed:
                return redirect("home")
            else:
                return redirect("profile_add")
        else:
            messages.error(request,"Erreur d'authentification")
    return  render(request,"accounts/login.html")

@login_required(login_url="login")
def profile_completed(request):
    user=request.user
    type=True if user.type=="STUDENT" else False

    if request.method=="POST":

        if type:
            student=user.student

            student.matricule=request.POST.get('matricule')
            student.filiere=request.POST.get('filiere')
            student.annee=request.POST.get('annee')

            student.bio=request.POST.get('bio')
            user.image = request.FILES['profil']

            student.save()
            user.is_completed=True
            user.save()
            return redirect("home")

        else:
            visiteur=user.visiteur
            visiteur.bio = request.POST.get('bio')
            user.image=request.FILES['profil']

            visiteur.save()
            user.is_completed=True
            user.save()
            return redirect("home")


    return render(request,"accounts/profile_register.html",{'user':request.user,"type":type})

def register(request):
    form=UserForm()
    if request.method=='POST':
        type=request.POST.get('type')

        form=UserForm(data=request.POST)

        if form.is_valid():
            #form.type=type

            form.save()
            messages.success(request,'Votre compte a été créé')
            return redirect('login')
        else:
            messages.error(request,form.errors)
    return  render(request,"accounts/register.html",context={"form":form})

@login_required(login_url='login')
def deconnection(request):
    logout(request)
    return redirect("home")

@login_required(login_url='login')
def profile(request):
    type = True if request.user.type == "STUDENT" else False
    post_videos=Video.objects.filter(user=request.user)
    context={'user':request.user,"post_videos":post_videos,'type':type}
    return render(request,"pages/profil.html",context)

def get_profile(request,pk):
    user=get_object_or_404(User,pk=pk)
    type = True if user.type == "STUDENT" else False
    post_videos=Video.objects.filter(user=user)
    context={'user':user,"post_videos":post_videos,'type':type}
    return render(request,"pages/profile_public.html",context)