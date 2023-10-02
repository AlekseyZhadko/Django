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
                            date_registration=datetime.date(random.randint(2010, 2023),
                                                            random.randint(1, 12),
                                                            random.randint(1, 30)), )
            client.save()
            for j in range(1, count + 1):
                product = Product(name=f'name{j}',
                                  description=f'Text from # {j} is bla bla bla many long text',
                                  price=random.randint(1, 10000) + random.randint(1, 100) / 100,
                                  count=random.randint(500, 2000),
                                  date_add=datetime.date(random.randint(2010, 2023),
                                                         random.randint(1, 12),
                                                         random.randint(1, 30)), )
                product.save()
                for k in range(1, count + 1):
                    products_all = Product.objects.all()
                    order = Order(client_id=client,
                                  sum=0)
                    order.save()
                    sum_order = 0
                    for _ in range(1, 10):
                        product_order = products_all[random.randint(1, len(products_all) - 1)]
                        product_order.count -= 1
                        sum_order += product_order.price
                        order.products.add(product_order)
                    order.sum = sum_order
                    order.save()
