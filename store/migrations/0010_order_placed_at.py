# Generated by Django 4.1.2 on 2022-11-09 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='placed_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
