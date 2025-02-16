from django.urls import path
from .views import menu, item_detail, add_to_cart

urlpatterns = [
    path('menu/', menu, name='menu'),  # URL for the menu page
    path('menu/item/<int:item_id>/', item_detail, name='item_detail'),  # URL for item detail
    path('menu/add/<int:item_id>/', add_to_cart, name='add_to_cart'),  # URL to add item to cart
]