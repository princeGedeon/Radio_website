from django import forms
from django.forms import ClearableFileInput

from Post_app.models import UploadFiles


class FilesUpload(forms.ModelForm):
    class Meta:
        model=UploadFiles
        fields=['files']
        widgets={
            'files':ClearableFileInput(attrs={'multiple':True})
        }