from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request):
    links_menu = {'links': [
        {'href': 'index', 'name': 'все'},
        {'href': 'index', 'name': 'дом'},
        {'href': 'index', 'name': 'офис'},
        {'href': 'index', 'name': 'модерн'},
        {'href': 'index', 'name': 'классика'},
    ]}
    return render(request, 'mainapp/products.html', context=links_menu)
