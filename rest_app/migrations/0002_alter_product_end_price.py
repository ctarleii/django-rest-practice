# Generated by Django 4.2.4 on 2023-08-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
