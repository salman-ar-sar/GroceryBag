# Generated by Django 3.1.5 on 2021-01-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
