# Generated by Django 3.2.8 on 2021-11-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211109_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='media/base/event'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
