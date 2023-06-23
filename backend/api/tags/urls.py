from django.urls import include, path
from rest_framework import routers

from .views import TagViewSet

router_v_1 = routers.DefaultRouter()
router_v_1.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router_v_1.urls)),
]
