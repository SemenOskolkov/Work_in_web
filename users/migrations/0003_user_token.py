# Generated by Django 4.1.5 on 2023-02-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='токен'),
        ),
    ]