# Generated by Django 5.1.2 on 2024-11-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_rename_orderdelivered_order_orderdelivered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderPackaging',
            field=models.BooleanField(default=False),
        ),
    ]
