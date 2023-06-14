from django.urls import path

from .views import FavoriteView, ShoppingCartView

urlpatterns = [
    path(
        'recipes/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='favorite'
    ),
    path(
        'recipes/<int:id>/shopping_cart/',
        ShoppingCartView.as_view(),
        name='shopping_cart'
    ),
]
