from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, Cart, CartItem, CategoryStock
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@csrf_exempt
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, cart_id=_cart_id(request))
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    category_stock = get_object_or_404(CategoryStock, cart=cart, category=product.category)

    print(cart_item.quantity, cart_item.product.stock , cart_item.category_stock.stock , product.category.quantity)
    if cart_item.quantity < cart_item.product.stock and cart_item.category_stock.stock > 0:
        print("paco")
        cart_item.quantity += 1
        cart_item.save()
        category_stock.stock -= 1
        category_stock.save()

    if cart_item.quantity == cart_item.product.stock and cart_item.category_stock.stock == 0:
        return JsonResponse({
            "status": False,
            "product": cart_item.quantity,
            "category": category_stock.stock,
            'name': product.category.name,
            'product_name': product.name,
            'cat': product.category.slug
        })

    return JsonResponse({
        "status": True,
        "product": cart_item.quantity,
        "category": cart_item.category_stock.stock,
        'name': product.category.name,
        'product_name': product.name,
        'cat': product.category.slug
    })


def cart_detail(request):
    category = Category.objects.all().order_by('order')

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

        products = Product.objects.filter(available=True)

        for product in products:
            cart_item = CartItem.objects.create(product=product, quantity=0, cart=cart,
                                                category_stock=CategoryStock.objects.get(cart=cart,
                                                                                         category=product.category))
            cart_item.save()

    category_stocks = CategoryStock.objects.filter(cart=cart)
    cart_items = CartItem.objects.filter(cart=cart, active=True).order_by('product')

    return render(request, 'store/cart.html',
                  dict(cart_items=cart_items, categorys=category, category_stock=category_stocks
                       ))


@csrf_exempt
def cart_remove(request, product_id):

    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    category_stock = CategoryStock.objects.get(cart=cart, category=product.category)

    if cart_item.quantity > 0 and cart_item.category_stock.stock < product.category.quantity:
        cart_item.quantity -= 1
        cart_item.save()
        category_stock.stock += 1
        category_stock.save()

    if cart_item.quantity == 0 or cart_item.category_stock.stock == product.category.quantity:
        return JsonResponse({
            "status": False,
            "product": cart_item.quantity,
            "quantity": product.category.quantity,
            "category": category_stock.stock,
            'name': product.category.name,
            'product_name': product.name,
            'cat': product.category.slug
        })

    return JsonResponse({
        "status": True,
        "product": cart_item.quantity,
        "category": cart_item.category_stock.stock,
        'name': product.category.name,
        'product_name': product.name,
        'cat': product.category.slug
    })


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


def shop(request):
    product_categories = Category.objects.all().order_by('order')
    categories = {}
    for product_category in product_categories:
        categories[product_category.name] = {
            'product': Product.objects.filter(category=product_category, available=True),
        }

    context = {

        'product_categories': product_categories,
        'categories': categories
    }
    return render(request, 'store/shop.html', context)


def payer(request):
    return render(request, 'store/product_detail.html',
                  context={'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})


def commande(request):
    return render(request, 'store/commande.html')

def test(request):
    return render(request, 'store/notmember.html')