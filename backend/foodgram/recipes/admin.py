from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, RecipeTag, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Настройки для тегов """

    list_display = ('name', 'slug', 'color')
    list_filter = ('name',)
    search_fields = ('name', 'slug', 'color')
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ Настройки для рецептов """

    list_display = ('name', 'cooking_time', 'pub_date', 'author')
    list_filter = ('name',)
    search_fields = ('name', 'text', 'cooking_time')
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Настройки для ингредиентов """

    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    search_fields = ('name', 'measurement_unit',)
    empty_value_display = '-пусто-'


@admin.register(RecipeTag)
class RecipeTagAdmin(admin.ModelAdmin):
    """ Настройки для связи тегов и рецептов """

    list_display = ('recipe', 'tag',)
    list_filter = ('recipe',)
    search_fields = ('recipe', 'tag',)
    empty_value_display = '-пусто-'


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    """ Настройки для связи ингредиентов и рецептов """

    list_display = ('recipe', 'ingredient',)
    list_filter = ('recipe',)
    search_fields = ('recipe', 'ingredient',)
    empty_value_display = '-пусто-'
