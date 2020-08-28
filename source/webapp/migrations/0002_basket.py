# Generated by Django 2.2 on 2020-08-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='webapp.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Корзина',
            },
        ),
    ]