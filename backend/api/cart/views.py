from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from api.pagination import PageLimitPagination
from cart.models import Favorite, ShoppingCart
from .serializers import ShoppingCartSerializer, WriteFavoriteSerializer
from .utils import add_obj, delete_obj


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageLimitPagination

    def post(self, request, id):
        return add_obj(request, id, Favorite, WriteFavoriteSerializer)

    def delete(self, request, id):
        return delete_obj(request, id, Favorite)


class ShoppingCartView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageLimitPagination

    def post(self, request, id):
        return add_obj(request, id, ShoppingCart, ShoppingCartSerializer)

    def delete(self, request, id):
        return delete_obj(request, id, ShoppingCart)
