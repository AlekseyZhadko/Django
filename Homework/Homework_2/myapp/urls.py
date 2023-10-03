from django.urls import path

from myapp import views

urlpatterns = [
    path('products/', views.get_product, name='get_product'),
    path('products_update/', views.update_product, name='update_product'),
    path('orders/<int:client_id>', views.get_orders, name='get_orders'),
    path('orders/<int:client_id>/week', views.get_orders_last_week, name='get_orders_last_week'),
    path('orders/<int:client_id>/month', views.get_orders_last_month, name='get_orders_last_month'),
    path('orders/<int:client_id>/year', views.get_orders_last_year, name='get_orders_last_year'),
]
