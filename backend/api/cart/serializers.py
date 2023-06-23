from django.contrib.auth import get_user_model
from rest_framework import serializers

from cart.models import Favorite, ShoppingCart
from recipes.models import Recipe

User = get_user_model()


class WriteFavoriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для записи в избранное. """

    class Meta:
        model = Favorite
        fields = ('user', 'recipe')

    def to_representation(self, instance):
        return ReadFavoriteSerializer(instance.recipe, context={
            'request': self.context.get('request')
        }).data


class ReadFavoriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для чтения избранных рецептов """

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class ShoppingCartSerializer(serializers.ModelSerializer):
    """ Сериализатор для корзины. """

    class Meta:
        model = ShoppingCart
        fields = ('user', 'recipe')

    def to_representation(self, instance):
        return ReadFavoriteSerializer(instance.recipe, context={
            'request': self.context.get('request')
        }).data
