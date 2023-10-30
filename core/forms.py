from django import forms
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    """form for adding a post"""
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ['title','text']
        label = {"text":''}