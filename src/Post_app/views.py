from django.shortcuts import render, redirect
from django.shortcuts import  get_object_or_404
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from Post_app.models import Video, CommentaireVideo, Audio, CommentaireAudio, Visuel, CommentaireVisuel


class ListPost(ListView):
    context_object_name = "objects"
    template_name = "pages/filter.html"

class CreateVideo(CreateView):
   model = Video
   template_name = "pages/formulaire.html"
   fields = ["title","desc","type","link_video"]
   success_url = reverse_lazy("video_create")

class CreateAudio(CreateView):
   model = Audio
   template_name = "pages/formulaire.html"
   fields = ["title","desc","type","link_audio"]
   success_url = reverse_lazy("audio_create")

class CreateImage(CreateView):
   model = Visuel
   template_name = "pages/formulaire.html"
   fields = ["title","desc","type","visuel"]
   success_url = reverse_lazy("image_create")

def detailVideo(request,slug):
    video=get_object_or_404(Video,slug=slug)
    video_cats=Video.objects.all()[0:8]
    commentaires=CommentaireVideo.objects.filter(video_post=video).filter(visible=True).order_by('-date')
    if request.user.is_authenticated:
        if request.method=='POST':
            content=request.POST.get('content')
            comment=CommentaireVideo.objects.create(message=content,user=request.user,video_post=video)
            comment.save()
            return redirect('detail_video',slug=slug)

    context={"video":video,"comments":commentaires,"video_cats":video_cats}
    return render(request,"pages/detail_video.html",context)

def detailAudio(request,slug):
    audio=get_object_or_404(Audio,slug=slug)
    audio_cats=Audio.objects.all()[0:8]
    commentaires=CommentaireAudio.objects.filter(audio_post=audio).filter(visible=True).order_by('-date')
    if request.user.is_authenticated:
        if request.method=='POST':
            content=request.POST.get('content')
            comment=CommentaireAudio.objects.create(message=content,user=request.user,audio_post=audio)
            comment.save()
            return redirect('detail_audio',slug=slug)

    context={"video":audio,"comments":commentaires,"video_cats":audio_cats}
    return render(request,"pages/detail_audio.html",context)


def detailImage(request,slug):
    image=get_object_or_404(Visuel,slug=slug)
    visuel_cats=Visuel.objects.all()[0:8]
    commentaires=CommentaireVisuel.objects.filter(visuel_post=image).filter(visible=True).order_by('-date')
    if request.user.is_authenticated:
        if request.method=='POST':
            content=request.POST.get('content')
            comment=CommentaireVisuel.objects.create(message=content,user=request.user,visuel_post=image)
            comment.save()
            return redirect('detail_image',slug=slug)

    context={"video":image,"comments":commentaires,"video_cats":visuel_cats}
    return render(request,"pages/detail_image.html",context)

