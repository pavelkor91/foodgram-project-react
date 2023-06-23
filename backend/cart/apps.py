from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
    verbose_name = 'Корзина/Избранное'
    verbose_name_plural = 'Корзины/Избранное'
