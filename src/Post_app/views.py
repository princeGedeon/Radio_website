from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.shortcuts import  get_object_or_404
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from Post_app.models import Video, CommentaireVideo, Audio, CommentaireAudio, Visuel, CommentaireVisuel


class ListPost(ListView):
    context_object_name = "objects"
    template_name = "pages/filter.html"
    paginate_by = 12



    def get_queryset(self):
        context_product = self.queryset
        types=self.request.GET.get("type")
        item = self.request.GET.get('search')
        sort = self.request.GET.get("tri")
        print(item)

        if item != '' and item is not None and item!=0:
            context_product = context_product.filter(title__icontains=item)
        if types=='0':
            pass
        else:
            context_product=context_product.filter(type=type)

        if sort=='0':
            pass
        else:
            if sort=="1":
                context_product=context_product.order_by('title')
            elif sort=="2":
                context_product=context_product.order_by('-title')


        return context_product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_queryset()

        return context


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

