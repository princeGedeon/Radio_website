from django.urls import path

from accounts.views import connection, deconnection

from accounts.views import register

urlpatterns = [
    path('login/',connection,name="login"),
    path('register/',register,name="register"),
    path('logout/',deconnection,name="logout")

]