# Generated by Django 4.0.3 on 2022-08-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
