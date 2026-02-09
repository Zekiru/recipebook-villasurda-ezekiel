from django.urls import path
from .views import PATH, index, RecipeListView, RecipeView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/1/', RecipeView.as_view(recipe_path = PATH.get('recipe1')), name='recipe-1'),
    path('recipe/2/', RecipeView.as_view(recipe_path = PATH.get('recipe2')), name='recipe-2'),
]