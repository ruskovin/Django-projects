# Generated by Django 4.2.2 on 2023-06-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to=''),
        ),
    ]
