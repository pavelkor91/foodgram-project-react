from django.urls import include, path
from rest_framework import routers

from .views import IngredientViewSet

router_v_1 = routers.DefaultRouter()
router_v_1.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router_v_1.urls)),
]
