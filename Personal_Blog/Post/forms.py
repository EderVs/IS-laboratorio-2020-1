from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    paragraph = forms.CharField(label='Paragraph', widget=forms.Textarea)
    image = forms.ImageField(label='Image')


#class PostForm(ModelForm):
#    class Meta:
#        model = Post
#        fields = ['title', 'paragraph', 'image']
