# Generated by Django 4.2.7 on 2023-11-14 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
    ]