from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'phone', 'address']
