# Generated by Django 4.1.2 on 2022-11-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
    ]
