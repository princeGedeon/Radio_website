from django.urls import path

from Post_app.views import detailVideo

urlpatterns = [
path("video/<str:slug>",detailVideo,name="detail_video")

]