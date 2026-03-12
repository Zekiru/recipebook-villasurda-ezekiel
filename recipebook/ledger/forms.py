from django import forms
from django.forms.models import inlineformset_factory

from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',]


IngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    fields=['ingredient', 'quantity'],
    extra=0,
    can_delete=False,
)

ImageFormSet = inlineformset_factory(
    Recipe, RecipeImage,
    fields=['image', 'description'],
    extra=0,
    can_delete=False,
)
