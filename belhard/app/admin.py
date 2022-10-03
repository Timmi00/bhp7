from django.contrib import admin
from .models import Category, Product, Order


class ProductTabularInline(admin.TabularInline):
    model = Product


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'TITLE'
    # site_url = '/admin',
    index_title = 'INDEX TITLE'
    empty_value_display = 'NOTHING'
    enable_nav_sidebar = True


appadmin = AppAdminSite(name='appadmin')

@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    actions = (make_published, make_unpublished)
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя род.категории или id категории'
    inlines = (ProductTabularInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    actions = (make_published, make_unpublished)
    list_display = ('title', 'article', 'count', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'заголовок/id/article/price'
    fieldsets = (
        ('основные настройки',
         {'fields': ('title', 'article', 'price', 'category'),
          'description': 'описание'
          }),
        ('Дополнительные настройки',
         {'fields': ('is_published', 'descr', 'count')
          })
    )
    list_editable = ('category', 'count')
    prepopulated_fields = {'descr': ('title', 'article')}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'Н.У'
    list_display = ('product', 'user', 'date_created', 'is_paid')
    list_filter = ('is_paid',)
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', )
    # search_fields = ('user', 'is_paid')
    # search_help_text = 'Введите имя пользователя'


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)
