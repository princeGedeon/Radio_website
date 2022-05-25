from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import ListView

from Post_app.forms import VisuelForm, VideoForm, AudioForm
from Post_app.models import Video, CommentaireVideo, Audio, CommentaireAudio, Visuel, CommentaireVisuel, Categorie


class ListPost(ListView):
    context_object_name = "objets"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('search')
        categorie = self.request.GET.get("categorie")
        tri = self.request.GET.get("tri")

        if search is not None and search != "":
            context['objets'] = context['objets'].filter(title__icontains=search)

        if categorie is not None and categorie != "" and categorie != "all":
            context['objets'] = context['objets'].filter(categorie=categorie)

        if tri is not None and tri != "" and tri!="all":

            if tri == "option1":
                context['objets'] = context['objets'].order_by('date_created')

            elif tri == "option2":
                context['objets'] = context['objets'].order_by('-date_created')

            elif tri == "option3":

                tmp = context['objets'].order_by('nbre_commentaire')
            elif tri == "option4":

                context['objets'] = context['objets'].order_by('-nbre_commentaire')

            elif tri == "option5":

                context['objets'] = context['objets'].order_by('title')

            elif tri == "option6":

                context['objets'] = context['objets'].order_by('-title')

        context['categories'] = Categorie.objects.filter()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(context['objets'], 20)

        try:
            context['objets'] = paginator.page(page)
        except PageNotAnInteger:
            context['objets'] = paginator.page(1)
        except EmptyPage:
            context['objets'] = paginator.page(paginator.num_pages)

        return context

        return context_product


def detailVideo(request, slug):
    video = get_object_or_404(Video, slug=slug)
    video_cats = Video.objects.all()[0:8]
    commentaires = CommentaireVideo.objects.filter(video_post=video).order_by('-date')
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST.get('content')
            comment = CommentaireVideo.objects.create(message=content, user=request.user, video_post=video)
            comment.save()
            return redirect('detail_video', slug=slug)

    context = {"video": video, "comments": commentaires, "video_cats": video_cats}
    return render(request, "pages/detail_video.html", context)


def detailAudio(request, slug):
    audio = get_object_or_404(Audio, slug=slug)
    audio_cats = Audio.objects.all()[0:8]
    commentaires = CommentaireAudio.objects.filter(audio_post=audio).order_by('-date')
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST.get('content')
            comment = CommentaireAudio.objects.create(message=content, user=request.user, audio_post=audio)
            comment.save()
            return redirect('detail_audio', slug=slug)

    context = {"video": audio, "comments": commentaires, "video_cats": audio_cats}
    return render(request, "pages/detail_audio.html", context)


def detailImage(request, slug):
    image = get_object_or_404(Visuel, slug=slug)
    visuel_cats = Visuel.objects.all()[0:8]
    commentaires = CommentaireVisuel.objects.filter(visuel_post=image).order_by('-date')
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST.get('content')
            comment = CommentaireVisuel.objects.create(message=content, user=request.user, visuel_post=image)
            comment.save()
            return redirect('detail_image', slug=slug)

    context = {"video": image, "comments": commentaires, "video_cats": visuel_cats}
    return render(request, "pages/detail_image.html", context)


def add_visuel(request):
    cats = Categorie.objects.all()
    if request.method=="POST":
        title=request.POST.get("title")
        desc=request.POST.get('desc')
        type=request.POST.get('type')
        categorie=request.POST.get('categorie')
        visuel=request.FILES['img']
        vis=Visuel.objects.create(title=title,desc=desc,type=type,visuel=visuel,user=request.user)
        for cat in categorie:
            vis.categorie.add(cat)
        vis.save()


    return render(request,"pages/formulaire_visuel.html",{"cats":cats})

def add_video(request):
    cats = Categorie.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get('desc')
        type = request.POST.get('type')
        categorie = request.POST.get('categorie')
        link = request.POST.get('link_video')
        vid = Video.objects.create(title=title, desc=desc, type=type, link_video=link, user=request.user)
        for cat in categorie:
            vid.categorie.add(cat)
        vid.save()

    return render(request,"pages/formulaire_video.html",{"cats":cats})

def add_audio(request):
    cats=Categorie.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get('desc')
        type = request.POST.get('type')
        categorie = request.POST.get('categorie')
        link = request.POST.get('link_audio')
        aud = Visuel.objects.create(title=title, desc=desc, type=type, link_audio=link, user=request.user)
        for cat in categorie:
            aud.categorie.add(cat)
        aud.save()

    return render(request,"pages/formulaire_audio.html",{"cats":cats})