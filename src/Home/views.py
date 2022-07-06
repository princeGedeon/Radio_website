from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Post_app.models import Video, Visuel, Audio
from accounts.models import User
from website_radio import settings


def home(request):
    video=Video.objects.all()[0:9]
    visuel = Visuel.objects.all()[0:9]
    audio =Audio.objects.all()[0:9]
    context={"videos":video,"audios":audio,"visuels":visuel,'n_inscrit':User.objects.count,'n_visuel':Visuel.objects.count,"n_video":Video.objects.count,'n_audio':Audio.objects.count}

    return render(request,"pages/index.html",context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    if request.method=="POST":
        nom=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(nom,email,message)
        send_mail(
            'Prise de contact',
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    return render(request,"pages/contact.html")