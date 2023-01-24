from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category = [
            {'category_name': 'Орехи',
             'description': 'Съедобные плоды, состоящие из скорлупы (твёрдой или мягкой) и съедобного ядра.'}
        ]

        category_list = []
        for item in category:
            category_list.append(Category(**item))

        Category.objects.bulk_create(category_list)
