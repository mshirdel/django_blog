# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Post


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-block-level'}),
            'content': forms.Textarea(attrs={'class': 'input-block-level'})
        }
        error_messages = {
            'title': {
                'required': 'لطفا تیتر پست را وارد نمایید'
            },
            'content': {
                'required': 'لطفا متن محتوای پست را وارد نمایید'
            }
        }
