from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products and include sorting and search queries """

    shop = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            shop = shop.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Enter a search term to get results.")
                return redirect(reverse('shop'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            shop = shop.filter(queries)

    context = {
        'shop': shop,
        'search-term': query,
        'current_categories': categories,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show single product info """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
