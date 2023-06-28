from django.shortcuts import render
from .models import Product
from django.views import View

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'product_list.html', context)

class CartItemCountView(View):
    def get(self, request):
        # Логика для подсчета количества товаров в корзине
        cart_item_count = 0
        context = {'cart_item_count': cart_item_count}
        return render(request, 'cart_item_count.html', context)