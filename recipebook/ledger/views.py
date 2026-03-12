from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import (
    RecipeForm,
    IngredientFormSet,
    ImageFormSet,
)

REDIRECT_LINK = 'login'


def index(request):
    return redirect(reverse('recipe_list'))


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
    redirect_field_name = REDIRECT_LINK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        context['recipe'] = recipe
        context['ingredients'] = recipe.ingredients.all()
        context['images'] = recipe.images.all()
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_form.html'
    context_object_name = 'recipe_create'
    redirect_field_name = REDIRECT_LINK

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_data = self.request.POST or None
        file_data = self.request.FILES or None

        context['ingredients'] = IngredientFormSet(
            post_data,
            prefix='ingredients',
        )
        context['images'] = ImageFormSet(
            post_data, file_data,
            prefix='images',
        )

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        images = context['images']

        if form.is_valid() and ingredients.is_valid() and images.is_valid():
            form.instance.author = self.request.user.profile
            self.object = form.save()

            ingredients.instance = self.object
            images.instance = self.object

            ingredients.save()
            images.save()

            return redirect(self.get_success_url())

        return self.form_invalid(form)
