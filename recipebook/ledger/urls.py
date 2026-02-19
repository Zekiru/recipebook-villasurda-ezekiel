from django.urls import path
from .views import PATH, index, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/1/', RecipeDetailView.as_view(static_path = PATH.get('recipe1')), name='recipe-1'),
    path('recipe/2/', RecipeDetailView.as_view(static_path = PATH.get('recipe2')), name='recipe-2'),
]