from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile, Wishlist
from shop.models import Product
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """Display the user's wishlist."""
    wishlist = Wishlist.objects.filter(user=request.user)
    template = 'profiles/profile_wishlist.html'
    context = {
        'wishlist': wishlist
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """Add item to the user's wishlist."""

    product = get_object_or_404(Product, id=product_id)
    user = request.user

    product = Wishlist.objects.get_or_create(product=product, user=user)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def remove_wish(request, wish_id):

    wish = get_object_or_404(Wishlist, pk=wish_id)
    wish.delete()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
