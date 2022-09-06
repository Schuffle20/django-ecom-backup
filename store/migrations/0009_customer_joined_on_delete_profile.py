# Generated by Django 4.0.4 on 2022-08-27 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_orderitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='joined_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
