from django.urls import path, include

from accounts.views import connection, deconnection, profile, profile_completed

from accounts.views import register
from django.contrib.auth import views
urlpatterns = [
    path('profil/',profile,name="profile"),
    path('accounts/',include('allauth.urls')),
    path('login/',connection,name="login"),
    path('register/',register,name="register"),
    path('logout/',deconnection,name="logout"),
    path('profil_completed/',profile_completed,name="profile_add"),

    path('reset_password', views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_send',views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>",views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete")
]