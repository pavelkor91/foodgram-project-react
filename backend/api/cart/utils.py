from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from recipes.models import Recipe


def add_obj(request, id, obj, serializer):
    data = {
        'user': request.user.id,
        'recipe': id
    }
    recipe = get_object_or_404(Recipe, id=id)
    if not obj.objects.filter(
            user=request.user, recipe=recipe
    ).exists():
        serializer = serializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
    return Response(
        {"Failed": "Рецепт уже добавлен!"},
        status=status.HTTP_400_BAD_REQUEST
    )


def delete_obj(request, id, obj):
    recipe = get_object_or_404(Recipe, id=id)
    if obj.objects.filter(user=request.user, recipe=recipe).exists():
        obj.objects.filter(user=request.user, recipe=recipe).delete()
        return Response(
            {"Success": "Рецепт удален!"},
            status=status.HTTP_204_NO_CONTENT
        )
    return Response(
        {"Failed": "Рецепт не найден!"},
        status=status.HTTP_400_BAD_REQUEST
    )
