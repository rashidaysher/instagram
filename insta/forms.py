from django import forms
from django.forms import ModelForm, fields
from .models import Post, Bio

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'location', 'caption']

class BioForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  

    dp = forms.ImageField(required=False)
    username = forms.CharField(max_length=500,required=True)
    first_name = forms.CharField(max_length=500, required=False)
    last_name = forms.CharField(max_length=500, required=False)
    phone = forms.CharField(max_length=20, required=False)
    bio= forms.CharField(required=False, widget=forms.Textarea())

