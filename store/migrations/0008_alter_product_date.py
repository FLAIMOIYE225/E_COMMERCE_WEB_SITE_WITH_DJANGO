# Generated by Django 5.1.2 on 2024-11-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_date_alter_category_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
