from django.db import models
from django.db.models import UniqueConstraint


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
