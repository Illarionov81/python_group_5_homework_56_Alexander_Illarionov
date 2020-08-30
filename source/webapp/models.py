from django.core.validators import MinValueValidator
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая техника'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, verbose_name='Категория',
                                choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    amount = models.IntegerField(verbose_name='Остаток', validators=[MinValueValidator(0)])
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.name} - {self.amount}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='product', on_delete=models.CASCADE, verbose_name='Продукт')
    amount = models.IntegerField(null=True, verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class ProductOrder(models.Model):
    order = models.ForeignKey('webapp.Order', related_name='order_product', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey('webapp.Product', related_name='product_order', on_delete=models.CASCADE, verbose_name='Товар')
    amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return "{} | {}".format(self.order, self.product)


class Order(models.Model):
    product = models.ManyToManyField('webapp.Product', related_name='order', through='webapp.ProductOrder',
                                     through_fields=('order', 'product'), blank=True)
    user_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    telephone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=200, null=False, blank=False, verbose_name='Адресс')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'