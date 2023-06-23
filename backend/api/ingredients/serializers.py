from rest_framework import serializers

from ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """ Сериализатор ингредиентов """

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')
