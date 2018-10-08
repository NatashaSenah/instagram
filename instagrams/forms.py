from django import forms
from .models import Image,Profile
class ImageForm(forms.ModelForm):
  
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'Profile']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user']