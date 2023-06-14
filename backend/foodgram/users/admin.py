from django.contrib import admin

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
