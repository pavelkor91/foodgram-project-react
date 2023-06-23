from django.contrib import admin
from rest_framework.authtoken.models import TokenProxy

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Настройки для Пользователей. """

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
