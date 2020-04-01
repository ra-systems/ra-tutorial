import random
import datetime
import pytz
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Generates data for simple sales app'

    def add_arguments(self, parser):
        parser.add_argument('--clients', type=int, action='store', help='Number of client to get generated, default 10')
        parser.add_argument('--product', type=int, action='store',
                            help='Number of products t0o get generated, default 10')
        parser.add_argument('--records', type=int, action='store', help='Number of records per day,  default 10')

    def handle(self, *args, **options):
        from ...models import Client, Product, SimpleSales
        from django.contrib.auth.models import User
        user_id = User.objects.first().pk
        client_count = options.get('clients', 10) or 10
        product_count = options.get('products', 10) or 10
        records_per_day = options.get('records', 10) or 10

        # Generating clients
        already_recorded = Client.objects.all().count()
        clients_needed = client_count - already_recorded
        if clients_needed > 0:
            for index in range(already_recorded, already_recorded + clients_needed):
                Client.objects.create(title=f'Client {index}', lastmod_user_id=user_id, slug=index)
            self.stdout.write(f'{clients_needed} client(s) created')

        # Product
        already_recorded = Product.objects.all().count()
        product_needed = product_count - already_recorded
        if product_needed > 0:
            for index in range(already_recorded, already_recorded + product_needed):
                Product.objects.create(title=f'Product {index}', lastmod_user_id=user_id, slug=index)
            self.stdout.write(f'{product_needed} product(s) created')

        # generating sales
        # we will generate 10 records per day for teh whole current year
        sdate = datetime.datetime(datetime.date.today().year, 1, 1)
        edate = datetime.datetime(datetime.date.today().year, 12, 31)

        client_ids = Client.objects.values_list('pk', flat=True)
        product_ids = Product.objects.values_list('pk', flat=True)

        delta = edate - sdate  # as timedelta
        for i in range(delta.days + 1):
            day = sdate + datetime.timedelta(days=i)
            day = pytz.utc.localize(day)
            for z in range(1, records_per_day):
                SimpleSales.objects.create(
                    doc_date=day,
                    product_id=random.choice(product_ids),
                    client_id=random.choice(client_ids),
                    quantity=random.randrange(1, 10),
                    price=random.randrange(1, 10),
                    lastmod_user_id=user_id
                )
            self.stdout.write('.', ending='')

        self.stdout.write('')
        self.stdout.write('Done')
