# Generated by Django 4.2.2 on 2023-06-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_article_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
