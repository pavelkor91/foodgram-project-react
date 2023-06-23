from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.pagination import PageLimitPagination
from users.models import Follow

from .serializers import (ReadSubscriptionsSerializer,
                          WriteSubscriptionSerializer)

User = get_user_model()


class SubscribeView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'author': id
        }
        serializer = WriteSubscriptionSerializer(
            data=data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = get_object_or_404(User, id=id)
        if Follow.objects.filter(
                user=request.user, author=author
        ).exists():
            subscription = get_object_or_404(
                Follow, user=request.user, author=author
            )
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SubscriptionsView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    pagination_class = PageLimitPagination

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(author__user=user)
        page = self.paginate_queryset(queryset)
        serializer = ReadSubscriptionsSerializer(
            page, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
