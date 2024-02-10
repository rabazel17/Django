from django.core.management.base import BaseCommand
from ht02app.models import Customer


class Command(BaseCommand):
    help = "Delete customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.delete()
        self.stdout.write(f'{customer}')