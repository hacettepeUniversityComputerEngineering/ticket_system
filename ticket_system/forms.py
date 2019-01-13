from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from user.models import User, UserType


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserType

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_onlyUser = True
        if commit:
            user.save()
        return user
