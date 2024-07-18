import random

from django.core.paginator import Paginator

from datetime import datetime
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from apps.cart.cart import Cart

from .models import Product, Category, ProductReview

def search(request):
    query = request.GET.get('query')
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)

    if instock:
        products = products.filter(num_available__gte=1)

    context = {
        'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'store/search.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    product.num_visits += 1
    product.save()

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)
        return redirect('product_detail', category_slug=category_slug, slug=slug)

    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))
    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)

    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)
    for image in product.images.all():
        imagesstring += "{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url)

    cart = Cart(request)
    product.in_cart = cart.has_product(product.id)

    context = {
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products,
        'variants': product.variants.all()
    }

    return render(request, 'store/product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)

    # Pagination
    paginator = Paginator(products, 10)  # Show 10 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': page_obj,  # Use page_obj instead of products
    }

    return render(request, 'store/category_detail.html', context)