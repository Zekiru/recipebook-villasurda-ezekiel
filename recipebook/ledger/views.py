import os, json
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Ingredient, Recipe, RecipeIngredient


def get_static_path(filename):
    return os.path.join(settings.BASE_DIR, 'static/data', filename)


PATH = {
    'list': get_static_path('recipe_list.json'),
    'recipe1': get_static_path('recipe_1.json'),
    'recipe2': get_static_path('recipe_2.json'),
}


def index(request):
    return redirect('recipes/list/')


def load_json_data(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: JSON file not found at {path}")
        return None


class RecipeListView(TemplateView):
    template_name = 'ledger/recipe_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Recipe.objects.all()
        return context


class RecipeDetailView(TemplateView):
    template_name = 'ledger/recipe_detail.html'
    static_path = PATH.get('recipe1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = load_json_data(self.static_path)
        return context
