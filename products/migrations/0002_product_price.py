# Generated by Django 4.1.1 on 2023-04-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='قیمت محصول'),
        ),
    ]
