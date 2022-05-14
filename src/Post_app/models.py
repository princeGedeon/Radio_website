from accounts.models import User

from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle=models.CharField(max_length=30)

    def __str__(self):
        return self.libelle

class Post(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    categorie=models.ManyToManyField(Categorie)
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=30)

    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Visuel(Post):
    visuel=models.ImageField(upload_to='post/visuel')


class Video(Post):
    link_video=models.URLField()


class Audio(Post):
    link_audio=models.URLField()


class Document(Post):
    doc=models.FileField(upload_to='post/file')


class CommentaireAudio(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    audio_post=models.ForeignKey(Audio,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return f"Commentaire de {self.user}"

class CommentaireVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    video_post=models.ForeignKey(Video,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return f"Commentaire de {self.user}"

class CommentaireVisuel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    visuel_post=models.ForeignKey(Visuel,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return f"Commentaire de {self.user}"


