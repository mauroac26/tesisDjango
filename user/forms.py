from django.contrib.auth.forms import UserCreationForm

from user.models import Users


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name','password1', 'password2', 'nivel']