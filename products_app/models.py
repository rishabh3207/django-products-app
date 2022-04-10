from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, primary_key=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=200, primary_key=True)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)
    product_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name