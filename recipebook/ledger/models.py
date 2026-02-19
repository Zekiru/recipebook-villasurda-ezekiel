from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
