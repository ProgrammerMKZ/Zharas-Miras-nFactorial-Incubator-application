from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registration_on_event

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)

        if commit==True:
            user.save()
        return user

class Registration_on_event_form(forms.ModelForm):
    class Meta:
        model = Registration_on_event
        fields = ['event']