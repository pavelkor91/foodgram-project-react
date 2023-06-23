from colorfield import fields
from django.db import models

from .validators import hex_validator


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
