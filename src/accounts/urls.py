from django.urls import path

from accounts.views import connection

from accounts.views import register

urlpatterns = [
    path('login/',connection,name="login"),
    path('register/',register,name="register"),

]