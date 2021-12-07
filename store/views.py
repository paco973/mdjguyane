from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem, CategoryStock
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        pass

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1

        cart_item.save()
        category_stock = CategoryStock.objects.get(cart=cart, category=product.category)
        category_stock.stock -= 1
        category_stock.save()

    except CartItem.DoesNotExist:
        pass
    return redirect('cart_detail')


def cart_detail(request):
    category = Category.objects.all()

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except ObjectDoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

        for categori in category:
            category_stock = CategoryStock.objects.create(cart=cart, category=categori, stock=categori.quantity)
            category_stock.save()

        products = Product.objects.all()

        for product in products:
            cart_item = CartItem.objects.create(product=product, quantity=0, cart=cart,
                                                category_stock=CategoryStock.objects.get(cart=cart,
                                                                                         category=product.category))
            cart_item.save()

    category_stocks = CategoryStock.objects.filter(cart=cart)
    cart_items = CartItem.objects.filter(cart=cart, active=True)

    return render(request, 'store/cart.html',
                  dict(cart_items=cart_items, categorys=category, category_stock=category_stocks
                       ))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.quantity -= 1
    cart_item.save()
    category_stock = CategoryStock.objects.get(cart=cart, category=product.category)
    category_stock.stock += 1
    category_stock.save()

    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


def shop(request):
    product_categories = Category.objects.all()
    categories = {}
    for product_category in product_categories:
        categories[product_category.name] = {
            'product': Product.objects.filter(category=product_category),
        }

    context = {

        'product_categories': product_categories,
        'categories': categories
    }
    return render(request, 'store/shop.html', context)


def payer(request):
    return render(request, 'store/product_detail.html', context={'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})
