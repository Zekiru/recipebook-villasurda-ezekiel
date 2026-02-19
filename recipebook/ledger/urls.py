from django.urls import path
from .views import index, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    path(
        'recipes/list/',
        RecipeListView.as_view(),
        name='recipe_list'
    ),
    path(
        'recipe/<int:recipe_id>/',
        RecipeDetailView.as_view(),
        name='recipe_detail'
    ),
]
