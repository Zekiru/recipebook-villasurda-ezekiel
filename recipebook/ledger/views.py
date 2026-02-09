from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the ledger index.")

def recipe_list(request):
    return HttpResponse("This is the recipe list view.")

def recipe_1(request):
    return HttpResponse("This is the recipe 1 view.")

def recipe_2(request):
    return HttpResponse("This is the recipe 2 view.")

# class RecipeListView(TemplateView):
#     template_name = 'ledger/recipe_list.html'


