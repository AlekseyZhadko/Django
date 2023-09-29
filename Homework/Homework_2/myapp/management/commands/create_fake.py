import datetime
import itertools
import random

from django.core.management.base import BaseCommand

from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake Client and Product, Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name{i}',
                            email=f'mail{i}@mail.ru',
                            phone_number=f'8800293{i}',
                            address=f'address{i}',
                            date_registration=datetime.date(1997, 10, 19), )
            client.save()
            for j in range(1, count + 1):
                product = Product(name=f'name{j}',
                                  description=f'Text from # {j} is bla bla bla many long text',
                                  price=122.22 + j,
                                  count=random.randint(1, 200),
                                  date_add=datetime.date(2023, 10, 19), )
                product.save()
                for k in range(1, count + 1):
                    products_all = Product.objects.all()
                    order = Order(client_id=client,
                                  sum=12131.12, )
                    order.save()
                    for _ in range(1, 10):
                        order.products.add(products_all[random.randint(1, len(products_all) - 1)])
                order.save()
