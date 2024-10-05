from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','media']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500',
                'placeholder': 'اكتب عنوان لمنشورك'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500',
                'placeholder': 'محتوى المنشور',
                'rows': 4
            }),
            'media': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500'
            })
        }
            