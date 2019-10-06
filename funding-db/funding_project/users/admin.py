from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'last_login']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


