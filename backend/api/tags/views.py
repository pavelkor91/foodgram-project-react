from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from tags.models import Tag

from .serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вьюсет тегов """

    permission_classes = [AllowAny, ]
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
