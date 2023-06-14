from django.urls import include, path

from .views import SubscribeView, SubscriptionsView

urlpatterns = [
    path(
        'users/<int:id>/subscribe/',
        SubscribeView.as_view(),
        name='subscribe'
    ),
    path(
        'users/subscriptions/',
        SubscriptionsView.as_view(),
        name='subscriptions'
    ),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]
