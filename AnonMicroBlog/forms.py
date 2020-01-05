from django import forms

from .models import PostModel


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ("post",)
        labels = {
            'post': 'Напишите пост',
        }
        widgets = {
            'post': forms.Textarea(attrs={'class': 'post-input'})
        }
