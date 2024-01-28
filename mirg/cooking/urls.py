from django.urls import path
from .views import *


urlpatterns = [
    path('<int:product_id>/', show_recipes_without_product),
]