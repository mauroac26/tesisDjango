from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.forms import fields

from user.models import Users


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2', 'nivel']

class editarUserForm(UserChangeForm):
    password = None
    class Meta:
        model = Users
        fields = ['nivel']


class editarPerfilForm(UserChangeForm):
    password = None
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'imagen']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file form-control-sm'  })
        }


class cambiarPasswordForm(PasswordChangeForm):
    model = Users
    fields = '__all__'
        