from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from tracker.forms import CustomUserCreationForm, CustomUserChangeForm
from tracker.models import CustomUser, Habit, Log, Comment


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name','email', 'username', 'profile_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Habit)
admin.site.register(Log)
admin.site.register(Comment)





  


