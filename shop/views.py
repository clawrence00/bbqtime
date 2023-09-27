from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products and include sorting and search queries """

    shop = Product.objects.all()

    context = {
        'shop': shop,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show single product info """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
