from django.urls import include, path

urlpatterns = [
    path('', include('api.users.urls')),
    path('', include('api.recipes.urls')),
    path('', include('api.cart.urls')),
    path('', include('api.tags.urls')),
    path('', include('api.ingredients.urls')),
]
