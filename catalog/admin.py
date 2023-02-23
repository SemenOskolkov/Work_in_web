from django.contrib import admin

from catalog.models import Category, Product, BlogRecord, Version

admin.site.register(BlogRecord)
admin.site.register(Version)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category',)
    search_field = ('product_name', 'description',)
    list_filter = ('category',)