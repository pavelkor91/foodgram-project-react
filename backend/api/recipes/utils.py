from django.db.models import Sum

from recipes.models import RecipeIngredient


def get_shop_list(user):
    ingredients = RecipeIngredient.objects.prefetch_related(
        'recipe', 'ingredient'
    ).filter(
        recipe__shopping_cart__user=user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    shop_list = '\n'.join([
        f"{ingredient['ingredient__name']} - {ingredient['amount']} "
        f"({ingredient['ingredient__measurement_unit']})"
        for ingredient in ingredients
    ])
    return f"Cписок покупок:\n{shop_list}"
