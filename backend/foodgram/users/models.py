from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    """ Модель пользователя """

    email = models.EmailField(
        verbose_name='E-mail',
        null=False,
        blank=False,
        max_length=254,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='username_email'
            ),
        ]

    def clean(self):
        if self.username == 'me':
            raise ValidationError('Имя me недоступно для регистрации')
        super(User, self).clean()


class Follow(models.Model):
    """ Модель подписки """

    user = models.ForeignKey(
        to='User',
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        to='User',
        related_name='author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='user_author_unique'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} стал подписчиком {self.author}'
