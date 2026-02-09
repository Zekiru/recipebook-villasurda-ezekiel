import os, json
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView

PATH = {
    'list': os.path.join(settings.BASE_DIR, 'static/data/recipe_list.json'),
    'recipe1': os.path.join(settings.BASE_DIR, 'static/data/recipe_1.json'),
    'recipe2': os.path.join(settings.BASE_DIR, 'static/data/recipe_2.json'),
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
        context['data'] = load_json_data(PATH.get('list'))
        return context


class RecipeView(TemplateView):
    template_name = 'ledger/recipe.html'
    recipe_path = PATH.get('recipe1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = load_json_data(self.recipe_path)
        return context
