from django.contrib import admin

# Register your models here.
from Student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['matricule','get_name',"filiere","annee"]

