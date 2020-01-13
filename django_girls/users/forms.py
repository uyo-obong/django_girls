from django.forms import Textarea, TextInput

from django_girls.users.models import RegisterUser
from django import forms


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=30)

    class Meta:
        model = RegisterUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        # widgets = {
        #     'first_name': TextInput(attrs={'class': 'form-control', 'label': 'jj', 'placeholder': 'test'}),
        # }


