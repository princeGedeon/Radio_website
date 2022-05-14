from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Type(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        VISITEUR="VISITEUR",'Visiteur'

    image = models.ImageField(upload_to="Student/profile", default=0)
    image_couverture = models.ImageField(upload_to="Student/couverture", default=0)
    email=models.EmailField(unique=True,blank=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    type=models.CharField(choices=Type.choices,max_length=255,default=Type.VISITEUR)
    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = ['phone','username']

    @property
    def date_joined_(self):
        reo
