# Generated by Django 3.2.8 on 2021-12-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_cartitem_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorystock',
            name='order',
            field=models.IntegerField(default=10000000),
        ),
    ]
