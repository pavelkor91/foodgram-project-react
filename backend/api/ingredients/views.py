from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ingredients.models import Ingredient
from .filters import IngredientFilter
from .serializers import IngredientSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет ингредиентов """

    permission_classes = [AllowAny, ]
    pagination_class = None
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = IngredientFilter
