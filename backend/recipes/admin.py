from django.contrib import admin

from .models import Recipe
from .forms import RequiredInlineFormSet


class IngredientsInline(admin.TabularInline):
    model = Recipe.ingredients.through
    formset = RequiredInlineFormSet
    verbose_name = 'Ингредиент'
    verbose_name_plural = "Ингредиенты"


class TagsInline(admin.TabularInline):
    model = Recipe.tags.through
    formset = RequiredInlineFormSet
    verbose_name = 'Тэг'
    verbose_name_plural = 'Тэги'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ Настройки для рецептов """

    list_display = ('name', 'cooking_time', 'pub_date', 'author', 'favorites')
    list_filter = ('tags',)
    search_fields = ('name', 'text', 'cooking_time')
    empty_value_display = '-пусто-'
    inlines = (
        IngredientsInline,
        TagsInline
    )

    @admin.display(description='Добавлено в избранное')
    def favorites(self, obj):
        return obj.favorites.count()
