from django.shortcuts import render, redirect
from django.shortcuts import  get_object_or_404
# Create your views here.
from django.views.generic import ListView

from Post_app.models import Video, CommentaireVideo, Audio, CommentaireAudio, Visuel, CommentaireVisuel


class ListPost(ListView):
    template_name = "pages/filter.html"

def detailVideo(request,slug):
    video=get_object_or_404(Video,slug=slug)
    video_cats=Video.objects.all()[0:8]
    commentaires=CommentaireVideo.objects.filter(video_post=video).order_by('-date')
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
    commentaires=CommentaireAudio.objects.filter(audio_post=audio).order_by('-date')
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
    commentaires=CommentaireVisuel.objects.filter(visuel_post=image).order_by('-date')
    if request.user.is_authenticated:
        if request.method=='POST':
            content=request.POST.get('content')
            comment=CommentaireVisuel.objects.create(message=content,user=request.user,visuel_post=image)
            comment.save()
            return redirect('detail_image',slug=slug)

    context={"video":image,"comments":commentaires,"video_cats":visuel_cats}
    return render(request,"pages/detail_image.html",context)

