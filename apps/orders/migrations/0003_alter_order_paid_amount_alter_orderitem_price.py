# Generated by Django 4.0.3 on 2022-08-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_paid_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
