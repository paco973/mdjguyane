from django.db import models


# Create your models here.


class Dotation(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Prénom')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nom')
    email = models.EmailField(verbose_name='Émail', blank=True, null=True, unique=True)
    dotation = models.IntegerField(verbose_name='don')
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Dotation'
        verbose_name_plural = 'Dotations'
