from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.forms import UserRegisterForm, editarUserForm
from .models import Users

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     # The forms to add and change user instances
#     form = UserRegisterForm
#     add_form = UserRegisterForm
#     model = Users

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('username', 'email', 'first_name', 'last_name',)
#     list_filter = ('groups', 'is_superuser', 'is_active', 'is_staff')
#     fieldsets = (
#         (None, {
#             'fields': ('username', 'password',)
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email', 'imagen')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active', 'is_staff', 'is_superuser',
#                 'groups', 'user_permissions'
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         })
#     )
#     add_fieldsets = (
#         (None, {
#             'fields': ('username', 'password1', 'password2',)
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email', 'imagen')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active', 'is_staff', 'is_superuser',
#                 'groups', 'user_permissions'
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         }),

#     )
#     add_fieldsets = ('groups','user_permissions')
#     search_fields = ('username',)
#     ordering = ('username',)
#     filter_horizontal = ()

# admin.site.register( Users, CustomUserAdmin)
admin.site.register(Users)