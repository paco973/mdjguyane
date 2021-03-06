# Generated by Django 3.2.8 on 2021-11-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Émail')),
                ('dotation', models.IntegerField(verbose_name='don')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Dotation',
                'verbose_name_plural': 'Dotations',
            },
        ),
    ]
