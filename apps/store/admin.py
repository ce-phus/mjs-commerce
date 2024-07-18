from django.contrib import admin
from .models import Category, Product, ProductImage, ProductReview

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductReviewInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
