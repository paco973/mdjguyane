# Generated by Django 3.2.8 on 2021-12-24 21:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211215_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdjmember',
            name='indentifiant',
            field=models.CharField(default=uuid.UUID('b5f37e77-bf9e-4e47-b144-d92003ad9f6e'), max_length=100, null=True),
        ),
    ]
