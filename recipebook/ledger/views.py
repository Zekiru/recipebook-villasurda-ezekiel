import os, json
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

def index(request):
    return redirect('recipes/list/')


recipe_list_path = os.path.join(settings.BASE_DIR, 'static/data/recipe_list.json')
recipe_1_path = os.path.join(settings.BASE_DIR, 'static/data/recipe_1.json')
recipe_2_path = os.path.join(settings.BASE_DIR, 'static/data/recipe_2.json')

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
        # json_file_path = os.path.join(settings.BASE_DIR, 'static/data/recipe_list_context.json')
        
        context['data'] = load_json_data(recipe_list_path)

        return context
    
class Recipe1View(TemplateView):
    template_name = 'ledger/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: Load recipe 1 data from JSON and add to context
        context['data'] = load_json_data(recipe_1_path)

        return context
    
class Recipe2View(TemplateView):
    template_name = 'ledger/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: Load recipe 2 data from JSON and add to context
        context['data'] = load_json_data(recipe_2_path)

        return context
    


