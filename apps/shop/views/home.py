from django.shortcuts import render

from shop.models import Product


def home_view(request):
    products = Product.objects.all()

    # Divide the items.price by 100 for each product
    for product in products:
        product.items.price /= 100

    context = {
        "products": products
    }

    return render(request, 'index.html', context)
