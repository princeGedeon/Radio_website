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
    list_filter = ("visible",)
    search_fields = ('user',"message")
@admin.register(CommentaireVisuel)
class CommentaireVisuelAdmin(admin.ModelAdmin):
    list_filter = ("visible",)
    search_fields = ('user', "message")
    list_display = ()
@admin.register(CommentaireAudio)
class CommentaireAudioAdmin(admin.ModelAdmin):
    list_filter = ("visible",)
    search_fields = ('user', "message")




