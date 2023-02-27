# Generated by Django 4.1.5 on 2023-02-26 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogrecord',
            options={'permissions': [('set_published_status', 'Can publish blog')], 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published_status', 'Can publish products'), ('can_change_description', 'Can change description'), ('can_change_category', 'Can change category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]