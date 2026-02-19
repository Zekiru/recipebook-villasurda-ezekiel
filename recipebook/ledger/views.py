from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Recipe, RecipeIngredient


def index(request):
    return redirect('recipes/list/')


class RecipeListView(TemplateView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        return context


class RecipeDetailView(TemplateView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(
            id=self.kwargs['recipe_id']
        )
        context['ingredients'] = RecipeIngredient.objects.filter(
            recipe_id=self.kwargs['recipe_id']
        )
        return context
