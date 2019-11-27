from django import forms

from .models import Bot

class PostForm(forms.ModelForm):

    class Meta:
        model = Bot
        fields = ('title', 'text',)