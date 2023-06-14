from colorfield import fields
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from .validators import hex_validator

User = get_user_model()


class Tag(models.Model):
    """ Теги для рецептов """

    name = models.CharField(
        verbose_name='Тег',
        max_length=200,
        unique=True
    )
    color = fields.ColorField(
        verbose_name='цвет в Hex',
        format='hex',
        default='#FFFFFF',
        help_text='Введите цвет в Hex формате',
        validators=[hex_validator,]
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
        max_length=200
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """ Описание ингридиентов """

    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredient_name_unit_unique'
            )
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """ Описание рецепта """

    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание рецепта'
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=[
            MinValueValidator(
                1, message='Время приготовления должно быть не менее 1 минуты'
            ),
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    ingredients = models.ManyToManyField(
        to='Ingredient',
        through='RecipeIngredient',
        verbose_name='Ингредиенты'
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='uploads/'
    )
    tags = models.ManyToManyField(
        to='Tag',
        through='RecipeTag',
        verbose_name='Тег',
        related_name='tags'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeTag(models.Model):
    """ Связь многие ко многим для тегов и рецептов """

    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    tag = models.ForeignKey(
        to='Tag',
        on_delete=models.CASCADE,
        verbose_name='Тег',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipe_tag_unique'
            )
        ]


class RecipeIngredient(models.Model):
    """ Связь многие ко многим для ингредиентов и рецептов """

    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        to='Ingredient',
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(
                1, message='Должно быть не менее 1 '
                           'ингридиента.'
            ),
        ]
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipe_ingredient_unique'
            )
        ]
