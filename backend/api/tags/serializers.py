from rest_framework import serializers

from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """ Сериализатор тегов """

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')
