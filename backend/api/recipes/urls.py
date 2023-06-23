from django.urls import include, path
from rest_framework import routers

from .views import RecipeViewSet

router_v_1 = routers.DefaultRouter()
router_v_1.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router_v_1.urls)),
]
