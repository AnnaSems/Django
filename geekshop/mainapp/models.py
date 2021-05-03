from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="имя",
        unique=True,
    )
    description = models.TextField(
        max_length=400,
        verbose_name='описание',
        blank=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=40,
    )
    image = models.ImageField(
        upload_to='products_img',
        verbose_name='краткое описание',
        blank=True,
    )
    description = models.TextField(
        max_length=400,
        verbose_name='описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена товара',
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество товара',
        default=0,
    )

    def __str__(self):
        return self.name
