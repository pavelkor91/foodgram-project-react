from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Настройки для тегов """

    list_display = ('name', 'slug', 'color')
    list_filter = ('name',)
    search_fields = ('name', 'slug', 'color')
    empty_value_display = '-пусто-'
