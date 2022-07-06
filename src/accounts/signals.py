from django.db.models.signals import post_save
from django.dispatch import receiver

from Student.models import Student, Visiteur
from accounts.models import User



@receiver(post_save,sender=User)
def post_save_created(sender,instance,created,**kwargs):
    if created:
        if instance.type==User.Type.STUDENT:
            Student.objects.create(user=instance)
        elif instance.type==User.Type.VISITEUR:
            Visiteur.objects.create(user=instance)


