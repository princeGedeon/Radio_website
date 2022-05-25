from django.utils.text import slugify

from accounts.models import User

from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle=models.CharField(max_length=255)

    def __str__(self):
        return self.libelle

class Post(models.Model):
    class Type(models.TextChoices):
        REPORTAGE = "Reportage","Reportage"
        DIVERTISSEMENT = 'Divertissement', "Divertissement"
        SCIENCE = 'Science', "Science"
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    categorie=models.ManyToManyField(Categorie)
    title=models.CharField(max_length=100,default="Aucun titre")
    desc=models.TextField(default="Pas de description",null=True)
    type=models.CharField(max_length=255,choices=Type.choices,default=Type.SCIENCE)
    nbre_commentaire=models.IntegerField(default=0)
    date_created=models.DateTimeField(auto_now_add=True)
    is_visible=models.BooleanField(default=False)

    class Meta:
        abstract=True

class Visuel(Post):
    visuel=models.ImageField(upload_to='post/visuel')
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(str(self.pk) + '_' + self.title)
        super().save(*args, **kwargs)

    @property
    def get_nmber_commentaire(self):
        return self.commentairevisuel_set.count()


class Video(Post):
    link_video=models.URLField()
    code_id=models.CharField(max_length=200,blank=True,null=True)
    slug=models.SlugField(max_length=255,blank=True,null=True)
    def save(self,*args,**kwargs):
        self.code_id=self.link_video.split('/')[-1]
        if not self.slug:
            self.slug=slugify(str(self.pk)+'_'+self.title)
        super().save(*args,**kwargs)

    @property
    def get_image(self):
        return f"https://img.youtube.com/vi/{self.code_id}/mqdefault.jpg"

    @property
    def get_nmber_commentaire(self):
        return self.commentairevideo_set.count()

class Audio(Post):
    link_audio=models.URLField()
    code_id = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.code_id = self.link_audio.split('/')[-1]
        if not self.slug:
            self.slug = slugify(str(self.pk) + '_' + self.title)
        super().save(*args, **kwargs)

    @property
    def get_nmber_commentaire(self):
        return self.commentaireaudio_set.count()
    @property
    def get_image(self):
        return f"https://img.youtube.com/vi/{self.code_id}/mqdefault.jpg"


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


