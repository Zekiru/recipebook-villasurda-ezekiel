from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(
        validators=[MinLengthValidator(256)],
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
        default=None
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
