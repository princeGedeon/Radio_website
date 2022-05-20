from django.urls import path

from Post_app.views import detailVideo, detailAudio, detailImage, ListPost

urlpatterns = [
path("video/<str:slug>",detailVideo,name="detail_video"),
path('audio/<str:slug>',detailAudio,name="detail_audio"),
path('visuel/<str:slug>',detailImage,name="detail_image"),
path("emission/tv",ListPost.as_view(queryset=[]),name="emission_tv"),
path("emission/radio",ListPost.as_view(queryset=[]),name="emission_radio"),
path("atelier/graphique",ListPost.as_view(queryset=[]),name="atelier_graphique"),

]