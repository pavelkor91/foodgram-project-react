from django.contrib import admin

from .models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Настройки для ингредиентов """

    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    search_fields = ('name', 'measurement_unit',)
    empty_value_display = '-пусто-'
