from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            {'product_name': 'Банан', 'description': 'Съедобный плод культивируемых растений рода Банан', 'preview': '',
             'category': 'Фрукты', 'purchase_price': '76.5'},
            {'product_name': 'Помидор',
             'description': 'Сочные плоды, как правило имеющие красный цвет и круглую форму.', 'preview': '',
             'category': 'Овощи', 'purchase_price': '68.9'},
            {'product_name': 'Арахис',
             'description': 'Вздутые овальные бобы, внутри которых заключены ядра, по три-четыре в каждом.',
             'preview': '', 'category': 'Орехи', 'purchase_price': '48.4'}
        ]

        products_list = []
        for item in products:
            products_list.append(Product(**item))

        Product.objects.bulk_create(products_list)
