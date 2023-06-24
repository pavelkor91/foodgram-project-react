from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import User

from .models import User


class UserAdmin(UserAdmin):
    """ Настройки для Пользователей. """

    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': (
                        'email', 
                        'username',
                        'first_name',
                        'last_name',
                        'password1', 
                        'password2'
                    ),
                },
            ),
    )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
    list_filter = ('username',)
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
    empty_value_display = '-пусто-'

admin.site.unregister(TokenProxy)
admin.site.register(User, UserAdmin)