# Generated by Django 4.0.4 on 2022-08-25 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='category',
        ),
    ]
