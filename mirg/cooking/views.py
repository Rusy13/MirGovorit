from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_recipes_without_product(request, product_id):
    return HttpResponse(f"Главная страница {product_id}")