from django.urls import path

from Post_app.models import Video,Audio,Visuel
from Post_app.views import detailVideo, detailAudio, detailImage, ListPost, CreateVideo, CreateAudio,CreateImage

urlpatterns = [
path("import_video",CreateVideo.as_view(),name="video_create"),
path("import_audio",CreateAudio.as_view(),name="audio_create"),
path("import_image",CreateImage.as_view(),name="image_create"),
path("video/<str:slug>",detailVideo,name="detail_video"),
path('audio/<str:slug>',detailAudio,name="detail_audio"),
path('visuel/<str:slug>',detailImage,name="detail_image"),
path("emission/tv",ListPost.as_view(queryset=Video.objects.filter(visible=True)),name="emission_tv"),
path("emission/radio",ListPost.as_view(queryset=Audio.objects.filter(visible=True)),name="emission_radio"),
path("atelier/graphique",ListPost.as_view(queryset=Visuel.objects.filter(visible=True)),name="atelier_graphique"),


]