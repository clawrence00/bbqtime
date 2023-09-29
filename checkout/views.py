from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('basket', {})
    if not bag:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NvmZyLUzhYEPKBM4LlTZfl9dAGF4UppzpjaG9axJADeYyEMCAIVzwr8TJnG6LB4wFfdAfLHfNNmh3S1hdooJPK700iEiNftxe',
        
    }

    return render(request, template, context)
