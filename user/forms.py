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
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


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
        self.fields['groups'] =  forms.ModelChoiceField(label= "Grupo", queryset=Group.objects.all(), initial=Group.objects.get(user = instance.id))
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class editarPerfilForm(UserChangeForm):
    password = None
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'imagen']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-sm' })
           
        }


class cambiarPasswordForm(PasswordChangeForm):
    class Meta:
        model = Users
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(cambiarPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'





class resetPasswordForm(forms.Form):
    password = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese una contraseña',
        'class': 'form-control form-control-sm',
        'autocomplete': 'off',
        'size': '25'
    }))

    confirmPassword = forms.CharField(label='Confirmación de contraseña nueva', widget=forms.PasswordInput(attrs={
        'placeholder': 'Repetir contraseña',
        'class': 'form-control form-control-sm',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']

        if password != confirmPassword:
            raise forms.ValidationError('Las contraseña deben ser iguales')
        return cleaned

    
    def __init__(self, *args, **kwargs):
        super(resetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
        