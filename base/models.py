from django.db import models
from django.urls import reverse


class Level(models.Model):
    name = models.CharField(max_length=10, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'


class City(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True, max_length=1250)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Study(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True, null=True, max_length=1250)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'Study'
        verbose_name_plural = 'Studies'


class Student(models.Model):
    last_name = models.CharField(max_length=20, blank=False, null=False)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    phone_number = models.CharField(max_length=13, unique=True, blank=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    address = models.CharField(max_length=100, blank=False, null=False)
    school = models.CharField(max_length=50, blank=False, null=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE, related_name='studies', null=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Volunteer(models.Model):
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    email = models.EmailField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    profession = models.CharField(max_length=100, blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # managed = True
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'


# À voir si je garde ou pas
class Event(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='media/base/event')
    slug = models.SlugField(blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def get_url(self):
        return reverse('detail', args=[self.slug])


# À voir si je garde ou pas
class EventByStudent(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='events')
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

    class Meta:
        # managed = True
        verbose_name = 'EventByStudent'
        verbose_name_plural = 'EventByStudents'


class Role(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    nombre = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class MdjMember(models.Model):
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Prénom')
    first_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nom')
    birthday = models.DateField(blank=True, null=True, verbose_name='Date_De_Naissance')
    description = models.TextField(blank=True, null=True, max_length=500, verbose_name='Description')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', null=True, verbose_name='Role')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='Ville')
    phone_number = models.CharField(max_length=13, unique=True, blank=False, verbose_name='Numéro_De_Téléphone')
    email = models.EmailField(blank=False, null=False, unique=True, verbose_name='Email')
    address = models.CharField(max_length=255, blank=False, null=False, verbose_name='Adresse')
    photo = models.ImageField(blank=True, null=True, upload_to='media/base/member', verbose_name='Photo')
    ordre = models.IntegerField(auto_created=True, verbose_name='Ordre', default=0)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # managed = True
        verbose_name = 'MdjMember'
        verbose_name_plural = 'MdjMembers'


class Message(models.Model):
    last_name = models.CharField(max_length=20, blank=False, null=False)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    message = models.TextField(max_length=1500)
    email = models.EmailField(blank=False, null=False, unique=True)
    see = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        # managed = True
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Newsletter(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        # managed = True
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class ProductCategory(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategory'


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


