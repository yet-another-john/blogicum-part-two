from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
