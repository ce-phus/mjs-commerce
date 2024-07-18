from django.shortcuts import render
from apps.store.models import Product, Category
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.filter(is_featured=True)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }

    return render(request, "core/index.html", context)

def allproducts(request):
    products_list = Product.objects.all()

    paginator = Paginator(products_list, 20)  
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
    }

    return render(request, "core/allproducts.html", context)