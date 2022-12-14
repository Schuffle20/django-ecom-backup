# Generated by Django 4.0.4 on 2022-09-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False, help_text='0=No Discount, 1=Discount'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=65, max_digits=7),
        ),
    ]
