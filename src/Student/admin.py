from django.contrib import admin

# Register your models here.
from Student.models import Student, Visiteur


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','get_name',"filiere","annee"]

@admin.register(Visiteur)
class VisiteurAdmin(admin.ModelAdmin):
    pass
