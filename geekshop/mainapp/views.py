from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.


def main(request):
    products = Product.objects.all()[:3]
    context = {
        'products': products,
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request):
    links_menu = ProductCategory.objects.all()
    product = Product.objects.get(id=2)
    return render(request, 'mainapp/products.html', context={'links_menu': links_menu,
                                                             'product': product})
