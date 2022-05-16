from django.urls import path

from Home.views import home, about, contact

urlpatterns = [
    path("",home,name="home"),
    path('about/',about,name="about"),
    path('contact-us/',contact,name="contact")
]