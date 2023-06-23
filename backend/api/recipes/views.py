from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.mixins import NoPutModelViewSet
from api.pagination import PageLimitPagination
from api.permissions import IsAdminOrOwnerOrReadOnly
from recipes.models import Recipe
from .filters import RecipeFilter
from .serializers import ReadRecipeSerializer, WriteRecipeSerializer
from .utils import get_shop_list


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
        if self.action == 'create':
            return WriteRecipeSerializer
        return ReadRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

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
