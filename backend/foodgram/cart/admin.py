from django.contrib import admin

from .models import Favorite, ShoppingCart


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """ Настройки для избранного """

    list_display = ('user', 'recipe',)
    list_filter = ('user',)
    search_fields = ('user', 'recipe',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """ Настройки для избранного """

    list_display = ('user', 'recipe',)
    list_filter = ('user',)
    search_fields = ('user', 'recipe',)
    empty_value_display = '-пусто-'
