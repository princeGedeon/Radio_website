from django.urls import path

from Post_app.views import upload_files

urlpatterns = [
    path('file/',upload_files),

]