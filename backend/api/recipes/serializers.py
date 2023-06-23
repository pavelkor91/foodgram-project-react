from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from cart.models import Favorite, ShoppingCart
from ingredients.models import Ingredient
from recipes.models import Recipe, RecipeIngredient, RecipeTag
from tags.models import Tag

from ..tags.serializers import TagSerializer
from ..users.serializers import CustomUserSerializer


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели отношения ингрелдиентов и рецептов """

    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'name', 'amount', 'measurement_unit')


class ReadRecipeSerializer(serializers.ModelSerializer):
    """ Сериализатор для чтения рецептов. """

    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializer()
    ingredients = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time',
            'ingredients'
        )

    def get_ingredients(self, obj):
        ingredients = RecipeIngredient.objects.select_related(
            'recipe', 'ingredient'
        ).filter(recipe=obj)
        return RecipeIngredientSerializer(ingredients, many=True).data

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Favorite.objects.select_related(
                'user', 'recipe'
            ).filter(
                user=request.user, recipe_id=obj.id
            ).exists()
        return False

    def get_is_in_shopping_cart(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return ShoppingCart.objects.select_related(
                'user', 'recipe'
            ).filter(
                user=request.user, recipe_id=obj
            ).exists()
        return False


class IngredientRecipeSerializer(serializers.ModelSerializer):
    """ Сериализатор добавления ингредиентов в рецепт """

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'amount')


class WriteRecipeSerializer(serializers.ModelSerializer):
    """ Сериализатор добавления рецепта """

    id = serializers.ReadOnlyField()
    ingredients = IngredientRecipeSerializer(many=True)
    author = CustomUserSerializer(read_only=True)
    image = Base64ImageField()
    tags_queryset = Tag.objects.all()
    tags = serializers.PrimaryKeyRelatedField(
        queryset=tags_queryset, many=True
    )

    class Meta:
        model = Recipe
        fields = (
            'id',
            'author',
            'ingredients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time'
        )

    def validate(self, data):
        ingredients = self.initial_data.get('ingredients')
        validated_ingredients = []
        if not ingredients:
            raise serializers.ValidationError(
                'Список ингредиентов не может быть пуст'
            )
        for ingredient in ingredients:
            if ingredient['id'] in validated_ingredients:
                raise serializers.ValidationError({
                    'Ингредиент уже добавлен в список!'
                })
            validated_ingredients.append(ingredient['id'])
        data['ingredients'] = ingredients
        return data

    def __update_tags_and_ingredients(self, tags, ingredients, instance):
        for tag in tags:
            RecipeTag.objects.create(recipe=instance, tag=tag)
        for ingredient in ingredients:
            obj = Ingredient.objects.get(pk=ingredient['id'])
            RecipeIngredient.objects.create(
                ingredient=obj,
                recipe=instance,
                amount=ingredient['amount']
            )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        author = self.context.get('request').user
        recipe = Recipe.objects.create(author=author, **validated_data)
        self.__update_tags_and_ingredients(tags, ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        RecipeTag.objects.filter(recipe=instance).delete()
        RecipeIngredient.objects.filter(recipe=instance).delete()
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        self.__update_tags_and_ingredients(tags, ingredients, instance)
        instance.name = validated_data.pop('name')
        instance.text = validated_data.pop('text')
        instance.image = validated_data.pop('image', instance.image)
        instance.cooking_time = validated_data.pop('cooking_time')
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return ReadRecipeSerializer(instance, context={
            'request': self.context.get('request')
        }).data
