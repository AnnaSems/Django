from django.core.management.base import BaseCommand
from ...models import ProductCategory, Product
from django.contrib.auth.models import User
from authapp.models import ShopUser

import json
import os

JSON_PATH = 'mainapp/JSON'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_id = product["category_id"]
            _category = ProductCategory.objects.get(id=category_id)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()


super_user = ShopUser.objects.create_superuser(
    'django', 'django@geekshop.local', '1234', age=33)
