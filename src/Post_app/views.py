from django.shortcuts import render, redirect
from django.shortcuts import  get_object_or_404
# Create your views here.
from Post_app.models import Video, CommentaireVideo


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
