# Generated by Django 3.2.8 on 2021-12-06 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='stock',
        ),
    ]