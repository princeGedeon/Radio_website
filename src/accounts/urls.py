from django.urls import path, include

from accounts.views import connection, deconnection, profile

from accounts.views import register
from django.contrib.auth import views
urlpatterns = [
    path('profil/',profile,name="profile"),
    path('accounts/',include('allauth.urls')),
    path('login/',connection,name="login"),
    path('register/',register,name="register"),
    path('logout/',deconnection,name="logout"),

    path('reset_password',views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent',views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]