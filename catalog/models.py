from django.db import models
from pytils.translit import slugify
from django.core.exceptions import ValidationError


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            ('set_published_status_products', 'Can publish products'),
            ('can_change_description', 'Can change description'),
            ('can_change_category', 'Can change category')
        ]

    def __str__(self):
        return f'{self.id} {self.product_name} {self.purchase_price} {self.category}'

    def save(self, *args, **kwargs):
        dont_use = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if self.product_name and self.description in dont_use:
            raise ValidationError('Запрещенное слово')
        else:
            super().save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.id} {self.category_name}'


class BlogRecord(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        (STATUS_ACTIVE, 'опубликован'),
        (STATUS_INACTIVE, 'не опубликован')
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_record/', **NULLABLE, verbose_name='Изображение')
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    sign_publication = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=10, verbose_name='Признак публикации')
    number_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

        permissions = [
            ('set_published_status_blog', 'Can publish blog')
        ]

    def __str__(self):
        return f'{self.id} {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogRecord, self).save(*args, **kwargs)


class Version(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        (STATUS_ACTIVE, 'активен'),
        (STATUS_INACTIVE, 'не активен')
    )

    product_name = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    version_status = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=10, verbose_name='Статус')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.product_name} {self.version_number} {self.version_name}'