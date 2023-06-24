from django.apps import AppConfig


class TagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'
    verbose_name = 'Тэг'
    verbose_name_plural = 'Тэги'
