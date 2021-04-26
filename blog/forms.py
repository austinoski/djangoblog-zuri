from django import forms
from django.contrib.auth.models import User

from .models import Comment


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
