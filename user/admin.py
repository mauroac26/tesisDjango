from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.forms import UserRegisterForm, editarUserForm
from .models import Users

# Register your models here.
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = editarUserForm
#     add_form = UserRegisterForm
#     model = Users

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     #list_display = ('email', 'nombre', 'apellido',)
#     #list_filter = ('nivel',)
#     fieldsets = (
#     (None, {'fields': ('username', 'nivel')}),
#     ('Informacion personal', {'fields': ('email', 'first_name', 'last_name','password')}),
#     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('email', 'first_name', 'last_name', 'nivel', 'username', 'password1', 'password2', 'groups','user_permissions'),
#     }),
#     #('Permisos', {'fields': ('groups','user_permissions')}),
#     )
#     search_fields = ('username',)
#     ordering = ('username',)
#     filter_horizontal = ()

# admin.site.register( Users, UserAdmin)
admin.site.register(Users)