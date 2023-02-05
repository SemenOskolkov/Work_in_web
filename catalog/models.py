from django.db import models
from pytils.translist import slugify


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.id} {self.product_name} {self.purchase_price} {self.category}'


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.id} {self.category_name}'


class BlogRecord(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_record/', **NULLABLE, verbose_name='Изображение')
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    sign_publication = models.BooleanField(verbose_name='Признак публикации')
    number_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.id} {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tittle)
        super(BlogRecord, self).save(*args, **kwargs)

