

from django.urls import path
from . import views
 
urlpatterns = [
    path('carousel/', views.carousel_view, name='index'),
    path('api/', views.CarouselItemList.as_view(), name='carousel-item-list'),
    path('api/<int:pk>/', views.CarouselItemDetail.as_view(), name='carousel-item-detail'),
]