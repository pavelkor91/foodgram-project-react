from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

from recipes.models import Recipe

User = get_user_model()


class Favorite(models.Model):
    """ Описание избранного """

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_favorite_unique'
            )
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    """ Модель корзины. """

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_shoppingcart_unique'
            )
        ]
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
