# Generated by Django 5.1.2 on 2024-11-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('notYetAccepted', 'Not Yet accepted'), ('orderAborted', 'Order Aborted'), ('orderAccepted', 'Order Accepted'), ('orderPackaged', 'Order Packaged'), ('orderDelivered', 'Order Delivered')], default='notYetAccepted', max_length=14),
        ),
    ]
