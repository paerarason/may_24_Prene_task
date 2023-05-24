from django.contrib.auth.models import User
from django import forms
class SignINForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class LoginINForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']