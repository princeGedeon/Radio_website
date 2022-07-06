
from django.db import models

# Create your models here.
from accounts.models import User




class Student(models.Model):
    FILIERE=(('IM','Internet et Multimédia'),('GL','Génie Logiciel'),('SI',"Sécurité Informatique"))
    ANNEE=(('L1','Licence1'),('L2','Licence2'),('L3','Licence3'),('M1','Master1'),('M2','Master2'),('D',"Diplomé"))
    matricule=models.CharField(max_length=30,unique=True,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")
    bio=models.TextField(blank=True)
    filiere=models.CharField(choices=FILIERE,blank=True,null=True,max_length=50)
    annee=models.CharField(max_length=15,choices=ANNEE)
    url=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.user.email
    @property
    def get_name(self):
        return f"{self.user.email.split('@')[0]}"


class Visiteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="visiteur")
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Visiteur {self.user}"
