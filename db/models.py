import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class Product(models.Model):
    upc = models.CharField(max_length = 4)
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return (self.name + " " + self.price)
