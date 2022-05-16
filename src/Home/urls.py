from django.urls import path

from Home.views import home, about, contact
from accounts.views import get_profile

urlpatterns = [
    path("",home,name="home"),
    path('about/',about,name="about"),
    path('contact-us/',contact,name="contact"),
    path('profil/<int:pk>/',get_profile,name="get_profil")
]