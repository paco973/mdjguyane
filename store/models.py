import email

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    quantity = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    order = models.IntegerField(default=10000000)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def apco(self):
        pass

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/products', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.cart_id


class CategoryStock(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        verbose_name = 'CategoryStock'
        verbose_name_plural = 'CategoryStocks'

    def __int__(self):
        return self.stock


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # stock = models.IntegerField(default=0)
    category_stock = models.ForeignKey(CategoryStock, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        return self.product.name
