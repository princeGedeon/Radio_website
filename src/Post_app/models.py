from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle=models.CharField(max_length=30)

    def __str__(self):
        return self.libelle

class Post(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    categorie=models.ManyToManyField(Categorie)
    desc=models.TextField(max_length=30)

    def __str__(self):
        return f"Publication de {self.user}"



class Commentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user}"

class Reponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    commmentaire=models.ForeignKey(Commentaire,on_delete=models.SET_NULL,null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reponse de {self.user} à {self.commmentaire.user}"

class UploadFiles(models.Model):
    files=models.FileField(upload_to='files/post',null=True)

