# Generated by Django 4.1.2 on 2022-11-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_promotion_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
