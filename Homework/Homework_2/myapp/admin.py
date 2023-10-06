from django.contrib import admin
from .models import Client, Product, Order


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'address', 'date_registration']
    ordering = ['id', '-name']
    list_filter = ['name', 'email', 'phone_number', 'address', 'date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Описание продукта (name)'


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'count', 'date_add']
    ordering = ['id', '-name']
    list_filter = ['name', 'price', 'count', 'date_add']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]
    # fields = ['id', 'name', 'price', 'count', 'date_add']
    readonly_fields = ['date_add']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),

        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description', 'image','date_add'],
            },
        ),

        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_id', 'sum', 'date']
    ordering = ['id', '-date']
    list_filter = ['client_id', 'sum', 'date']
    search_fields = ['client_id']
    search_help_text = 'Поиск по полю Описание продукта (client_id)'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
