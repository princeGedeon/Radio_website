from django.contrib import admin

# Register your models here.
from Post_app.models import Categorie, Post, Commentaire, UploadFiles, Reponse


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass
@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    pass
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadFiles)
class UploadFileAdmin(admin.ModelAdmin):
    pass

