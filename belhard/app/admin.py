from django.contrib import admin
from .models import Category, Product, TableOrder


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя род.категории или id категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'заголовок/id/article/price'


@admin.register(TableOrder)
class TableOrderAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    list_display = ('user', 'date_created', 'is_paid')
    list_filter = ('is_paid', 'user')
    search_fields = ('user', 'is_paid')
    search_help_text = 'Введите имя пользователя'
# admin.site.register(Category, CategoryAdmin)
