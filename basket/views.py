from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def view_basket(request):
    """ A view that renders the basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def update_basket(request, item_id):
    """ Update quantity of a specified product to the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a specified product to the basket """
    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
