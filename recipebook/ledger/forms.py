from django import forms
from django.forms.models import inlineformset_factory

from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',]


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['description'].required = False


IngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    fields=['ingredient', 'quantity'],
    extra=1,
    can_delete=False,
)

ImageFormSet = inlineformset_factory(
    Recipe, RecipeImage,
    fields=['image', 'description'],
    extra=1,
    can_delete=False,
)
