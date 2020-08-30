# Generated by Django 2.2 on 2020-08-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200828_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('telephone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адресс')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='webapp.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='webapp.Product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='order', through='webapp.ProductOrder', to='webapp.Product'),
        ),
    ]
