from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.mixins import NoPutModelViewSet
from api.pagination import PageLimitPagination
from api.permissions import IsAdminOrOwnerOrReadOnly
from recipes.models import Ingredient, Recipe, Tag

from .filters import IngredientFilter, RecipeFilter
from .serializers import (IngredientSerializer, ReadRecipeSerializer,
                          TagSerializer, WriteRecipeSerializer)
from .utils import get_shop_list


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет тегов """

    permission_classes = [AllowAny, ]
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет ингредиентов """

    permission_classes = [AllowAny, ]
    pagination_class = None
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [IngredientFilter, ]
    search_fields = ['name', ]


class RecipeViewSet(NoPutModelViewSet):
    """ Вьюсет для рецептов """

    permission_classes = [IsAdminOrOwnerOrReadOnly, ]
    queryset = Recipe.objects.prefetch_related(
        'ingredients', 'author'
    ).all()
    filterset_class = RecipeFilter
    filter_backends = [DjangoFilterBackend, ]
    pagination_class = PageLimitPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadRecipeSerializer
        return WriteRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def perform_destroy(self, instance):
        instance.delete()

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsAuthenticated, ]
    )
    def download_shopping_cart(self, request):
        grocery_list = get_shop_list(request.user)
        filename = 'shop_list.txt'
        response = HttpResponse(grocery_list, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
