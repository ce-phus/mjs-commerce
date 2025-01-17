import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product
from apps.cart.cart import Cart

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    print("Product ID", data)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    print("Added to cart")
    return JsonResponse(jsonresponse)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id= str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)