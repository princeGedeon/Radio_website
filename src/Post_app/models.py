from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)



class Commentaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

