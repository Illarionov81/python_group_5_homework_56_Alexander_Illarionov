# Generated by Django 2.2 on 2020-09-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_basket_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='session',
        ),
    ]