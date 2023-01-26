from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        products = [
            {'product_name': 'Банан', 'description': 'Съедобный плод культивируемых растений рода Банан', 'preview': '',
             'category': 'Фрукты', 'purchase_price': '76'}
        ]
        # Пример заполнения БД с существующими категориями
        # products = [
        #     {'product_name': 'Банан', 'description': 'Съедобный плод культивируемых растений рода Банан', 'preview': '',
        #      'category': 'Фрукты', 'purchase_price': '76'},
        #     {'product_name': 'Помидор',
        #      'description': 'Сочные плоды, как правило имеющие красный цвет и круглую форму.', 'preview': '',
        #      'category': 'Овощи', 'purchase_price': '68'},
        #     {'product_name': 'Арахис',
        #      'description': 'Вздутые овальные бобы, внутри которых заключены ядра, по три-четыре в каждом.',
        #      'preview': '', 'category': 'Орехи', 'purchase_price': '48'}
        # ]

        products_list = []
        for item in products:
            category = Category.objects.filter(category_name=item.get('category')).get()
            item['category'] = category
            product = Product(**item)
            products_list.append(product)

        Product.objects.bulk_create(products_list)
