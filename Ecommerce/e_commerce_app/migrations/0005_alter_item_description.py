# Generated by Django 4.2.2 on 2023-06-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(),
        ),
    ]
