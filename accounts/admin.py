from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomuserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomuserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)