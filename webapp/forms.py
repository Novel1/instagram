from django import forms
from django.forms import TextInput

from posts.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'class': 'form-control me-2 p-3', 'placeholder': 'Добавьте комментарий...'})
        }
        labels = {
            'text': ''
        }