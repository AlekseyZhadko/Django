from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.timezone import now

from myapp.models import Order, Product
from myapp.forms import Product_form


# Create your views here.
def get_product(request):
    products = Product.objects.filter()
    context = {
        'products': products,
    }
    return render(request, 'myapp/products.html', context=context)


def get_orders(request, client_id):
    orders = Order.objects.filter(client_id=client_id)
    context = {
        'orders': orders,
    }
    return render(request, 'myapp/orders.html', context=context)


def get_orders_last_week(request, client_id):
    year, week, _ = now().isocalendar()
    orders = Order.objects.filter(client_id=client_id, date__week=week)
    context = {
        'orders': orders,
    }
    return render(request, 'myapp/orders.html', context=context)


def get_orders_last_month(request, client_id):
    year, week, _ = now().isocalendar()
    month = int(week / 4)
    orders = Order.objects.filter(client_id=client_id, date__month=month)
    context = {
        'orders': orders,
    }
    return render(request, 'myapp/orders.html', context=context)


def get_orders_last_year(request, client_id):
    year, week, _ = now().isocalendar()
    orders = Order.objects.filter(client_id=client_id, date__year=year)
    context = {
        'orders': orders,
    }
    return render(request, 'myapp/orders.html', context=context)


def update_product(request):
    products = Product.objects.filter()
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']

            product = Product.objects.filter(id=int(id)).first()
            product.name = name
            product.description = description
            product.price = price
            product.count = count
            product.image = image
            product.save()
    else:
        form = Product_form()
    return render(request, 'myapp/products_update.html', {'form': form, 'products': products, })
