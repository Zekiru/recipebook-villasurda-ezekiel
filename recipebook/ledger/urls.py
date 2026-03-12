from django.urls import path
from .views import (
    index,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeAddImageView,
)

urlpatterns = [
    path('', index, name='index'),
    path(
        'recipes/list/',
        RecipeListView.as_view(),
        name='recipe_list'
    ),
    path(
        'recipe/<int:pk>/',
        RecipeDetailView.as_view(),
        name='recipe_detail'
    ),
    path(
        'recipe/add/',
        RecipeCreateView.as_view(),
        name='recipe_create'
    ),
    path(
        'recipe/<int:pk>/add_image',
        RecipeAddImageView.as_view(),
        name='recipe_add_image'
    ),
]
