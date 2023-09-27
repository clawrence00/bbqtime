from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products and include sorting and search queries """

    shop = Product.objects.all()

    context = {
        'shop': shop,
    }

    return render(request, 'shop/shop.html', context)
