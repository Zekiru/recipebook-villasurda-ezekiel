from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Recipe, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin


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


class RecipeDetailView(LoginRequiredMixin, TemplateView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe_detail'
    redirect_field_name = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        context['recipe'] = recipe
        context['ingredients'] = recipe.ingredients.all()
        return context
