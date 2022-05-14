from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Post_app.models import Video, Visuel, Audio
from accounts.models import User


def home(request):
    video=Video.objects.all()[0:6]
    visuel = Visuel.objects.all()[0:6]
    audio =Audio.objects.all()[0:6]
    context={"videos":video,"audios":audio,"visuels":visuel,'n_inscrit':User.objects.count,'n_visuel':Visuel.objects.count,"n_video":Video.objects.count,'n_audio':Audio.objects.count}

    return render(request,"pages/index.html",context)