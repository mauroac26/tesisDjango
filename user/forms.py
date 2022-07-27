from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group


from user.models import Users


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2', 'groups']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'password1': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'password2': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            
        }
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['groups'] =  forms.ModelChoiceField(queryset=Group.objects.all())

class editarUserForm(UserChangeForm):
    password = None
    class Meta:
        model = Users
        fields = ['groups']
        # widgets = {
        #     'groups': forms.ChoiceField()
        # }
    def __init__(self, instance, *args, **kwargs):
        
        super(editarUserForm, self).__init__(*args, **kwargs)
        self.fields['groups'] =  forms.ModelChoiceField(queryset=Group.objects.all(), initial=Group.objects.get(user = instance.id))

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
        