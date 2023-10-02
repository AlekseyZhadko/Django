from django.shortcuts import render
from django.utils.timezone import now

from myapp.models import Order


# Create your views here.

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
    month = int(week/4)
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
