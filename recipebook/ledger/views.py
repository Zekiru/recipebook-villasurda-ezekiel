from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the ledger index.")


