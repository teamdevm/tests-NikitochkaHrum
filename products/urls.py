from django.urls import path
from products.views import ProductListView, CartItemCountView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('cart/', CartItemCountView.as_view(), name='cart_item_count'),
]
