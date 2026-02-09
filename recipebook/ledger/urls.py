from django.urls import path
from .views import index, RecipeListView, Recipe1View, Recipe2View

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/1/', Recipe1View.as_view(), name='recipe-1'),
    path('recipe/2/', Recipe2View.as_view(), name='recipe-2'),
]