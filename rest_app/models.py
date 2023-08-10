from django.db import models


class Product(models.Model):
    discount_choices = (
        (0, '0 percent discount'),
        (10, '10 percent discount'),
        (15, '15 percent discount'),
        (20, '20 percent discount'),
        (30, '30 percent discount'),
        (50, '50 percent discount'),
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    end_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    discount = models.IntegerField(default=0, blank=True, choices=discount_choices)

    def save(self, *args, **kwargs):
        self.end_price = int(self.price * (100 - self.discount) / 100)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.title} - {self.price}'


class Category(models.Model):
    cat_name = models.CharField(max_length=255, verbose_name='cat_name')
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cat_name
