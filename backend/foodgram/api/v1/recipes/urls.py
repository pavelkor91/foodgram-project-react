from django.urls import include, path
from rest_framework import routers

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

router_v_1 = routers.DefaultRouter()
router_v_1.register('tags', TagViewSet, basename='tags')
router_v_1.register('ingredients', IngredientViewSet, basename='ingredients')
router_v_1.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router_v_1.urls)),
]
