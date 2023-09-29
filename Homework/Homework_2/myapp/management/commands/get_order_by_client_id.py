from django.core.management.base import BaseCommand
from myapp.models import Client, Order, Product


class Command(BaseCommand):
    help = "Get all order by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            orders = Order.objects.filter(client_id=client)
            intro = f'All order of {client.name}\n'
            text = '\n'.join(str(order.sum) + ' ' + str(order.date) for order in orders)
            self.stdout.write(f'{intro}{text}')
