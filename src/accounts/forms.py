from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']