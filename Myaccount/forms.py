from django import forms
from .models import User

class ProfileForm(forms.Form):
 class Meta:
  model = User
  fields = ['nickname', 'link', 'avatar']