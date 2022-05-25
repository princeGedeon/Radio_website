from django.db.models.signals import post_save
from django.dispatch import receiver

from Post_app.models import CommentaireVideo, CommentaireAudio, CommentaireVisuel


@receiver(post_save,sender=CommentaireVideo)
def post_save_created(sender,instance,created,**kwargs):
    if created:
        a=instance.video_post
        a.nbre_commentaire=a.get_nmber_commentaire
        a.save()

@receiver(post_save,sender=CommentaireVisuel)
def post_save_created(sender,instance,created,**kwargs):
    if created:
        a=instance.visuel_post
        a.nbre_commentaire=a.get_nmber_commentaire
        a.save()

@receiver(post_save,sender=CommentaireAudio)
def post_save_created(sender,instance,created,**kwargs):
    if created:
        a=instance.audio_post
        a.nbre_commentaire=a.get_nmber_commentaire
        a.save()