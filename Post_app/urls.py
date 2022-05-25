from django.urls import path

from Post_app.models import Video, Audio, Visuel
from Post_app.views import detailVideo, detailAudio, detailImage, ListPost, add_video, add_visuel, add_audio

urlpatterns = [
path("video/<str:slug>",detailVideo,name="detail_video"),
path('audio/<str:slug>',detailAudio,name="detail_audio"),
path('visuel/<str:slug>',detailImage,name="detail_image"),
path("emission/tv",ListPost.as_view(queryset=Video.objects.filter(is_visible=True),template_name = "pages/filter_tv.html"),name="emission_tv"),
path("emission/radio",ListPost.as_view(queryset=Audio.objects.filter(is_visible=True),template_name = "pages/filter_radio.html"),name="emission_radio"),
path("atelier/graphique",ListPost.as_view(queryset=Visuel.objects.filter(is_visible=True),template_name = "pages/filter_graphique.html"),name="atelier_graphique"),
path("add/video",add_video,name="add_video"),
path("add/visuel",add_visuel,name="add_visuel"),
path("add/audio",add_audio,name="add_audio"),

]