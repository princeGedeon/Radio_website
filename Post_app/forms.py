from django import forms

from Post_app.models import Video, Visuel, Audio


class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['title','desc','type','categorie','link_video']

class VisuelForm(forms.ModelForm):
    class Meta:
        model=Visuel
        fields=['title','desc','type','categorie','visuel']

class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio
        fields=['title','desc','type','categorie','link_audio']