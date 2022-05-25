from django.contrib import admin

# Register your models here.
from Post_app.models import Categorie, Visuel,CommentaireVideo,CommentaireAudio,CommentaireVisuel,Video,Visuel,Audio,Document

@admin.register(Document)
@admin.register(Visuel)
@admin.register(Video)
@admin.register(Audio)
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass
@admin.register(CommentaireVideo)
class CommentaireVideoAdmin(admin.ModelAdmin):
    pass
@admin.register(CommentaireVisuel)
class CommentaireVisuelAdmin(admin.ModelAdmin):
    pass
@admin.register(CommentaireAudio)
class CommentaireAudioAdmin(admin.ModelAdmin):
    pass




