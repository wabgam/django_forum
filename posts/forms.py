from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

