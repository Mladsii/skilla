from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'autor',

            'st_or_nw',
            'header_post',
            'test_post',
            'rating',
            'category',
        ]