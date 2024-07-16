from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.core.views import index, allproducts
from django.contrib.auth import views as auth_views
from apps.userprofile.views import myaccount, signup, logout
from apps.store.views import category_detail, search, product_detail
from apps.store.api import api_add_to_cart, api_remove_from_cart
from apps.coupon.api import api_can_use
from apps.cart.views import cart_detail, success
from apps.payment.views import initiate_payment, verify_payment
from apps.carousel.views import CarouselItemList
from apps.contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
    path('cart/', cart_detail, name='cart'),
    path('cart/success/', success, name='success'),
    path('', index, name='index'),
    path('index/allproducts/', allproducts, name='all_products'),
    path('', include('admin_material.urls')),
    path('contact/', contact, name='contact'),

    # Auth
    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', logout, name='logout'),

    # API
    path('api/', CarouselItemList.as_view(), name='carousel-item-list'),
    path('verify_payment<str:ref>/', verify_payment, name='verify_payment'),
    path('api/initiate_payment/', initiate_payment, name='initiate_payment'),
    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),

    # Store
    path('search/', search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('store/category/<slug:slug>/', category_detail, name='category_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
