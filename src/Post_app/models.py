from django.urls import reverse
from django.utils.text import slugify

from accounts.models import User

from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle=models.CharField(max_length=30)

    def __str__(self):
        return self.libelle

class Post(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    #categorie=models.ManyToManyField(Categorie,verbose_name="tags")
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=30)
    type=models.CharField(max_length=20,choices=(("Reportage","Reportage"),("Divertissement","Divertissement"),("Science","Science")),default=("Science","Science"))

    date_created=models.DateTimeField(auto_now_add=True)
    visible=models.BooleanField(default=True)

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
    def get_image(self):
        return self.visuel.url

    @property
    def get_detail(self):
        return reverse("detail_image",kwargs={"slug":self.slug})
class Video(Post):
    link_video=models.URLField()
    code_id=models.CharField(max_length=200,blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        self.code_id=self.link_video.split('/')[-1]
        if not self.slug:
            self.slug=slugify(str(self.pk)+'_'+self.title)
        super().save(*args,**kwargs)

    @property
    def get_detail(self):
        return reverse("detail_video",kwargs={"slug":self.slug})

    @property
    def get_image(self):
        return f"https://img.youtube.com/vi/{self.code_id}/mqdefault.jpg"


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
    def get_detail(self):
        return reverse("detail_audio",kwargs={"slug":self.slug})

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
    visible=models.BooleanField(default=True)


    def __str__(self):
        return f"Commentaire de {self.user}"


class CommentaireVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    video_post=models.ForeignKey(Video,on_delete=models.SET_NULL,null=True,blank=True)
    visible = models.BooleanField(default=True)


    def __str__(self):
        return f"Commentaire de {self.user}"

class CommentaireVisuel(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    visuel_post=models.ForeignKey(Visuel,on_delete=models.SET_NULL,null=True,blank=True)
    visible = models.BooleanField(default=True)


    def __str__(self):
        return f"Commentaire de {self.user}"


