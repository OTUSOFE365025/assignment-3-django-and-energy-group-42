############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

#For the ui
import tkinter as tk

# setup django environment
import django

from django.core.management import call_command

django.setup()

# Import your models for use in your script
from db.models import *

call_command("makemigrations", "db", interactive=False, verbosity=0)
call_command("migrate", interactive=False, verbosity=0)

############################################################################
## START OF APPLICATION
############################################################################

#Populate DB
Product.objects.update_or_create(upc="1234", defaults={"name": "Apple", "price": 1.99})
Product.objects.update_or_create(upc="5678", defaults={"name": "Orange", "price": 2.99})
Product.objects.update_or_create(upc="9123", defaults={"name": "Cantalope", "price": 3.99})
Product.objects.update_or_create(upc="4567", defaults={"name": "Melon", "price": 4.99})

#Scan function
def scanProducts():
    upcEntered = upcEntry.get()

    try:
        product = Product.objects.get(upc = upcEntered)
        productList.insert(tk.END, product.name + " $" + str(product.price))
    
    except Product.DoesNotExist:
        productList.insert(tk.END, "Unkown UPC entered")
    return 0

#Display items and enter them
root = tk.Tk()
root.title("Scanner")

tk.Label(root, text = "UPC: ").grid(row = 0, column = 0, padx = 10, pady = 10)
upcEntry = tk.Entry(root)
upcEntry.grid(row = 0, column = 1, padx = 1, pady = 10)

scanButton = tk.Button(root, text = "Scan Item", command = scanProducts)
scanButton.grid(row = 0, column = 2, padx = 10, pady = 10)

productList = tk.Listbox(root, width = 50)
productList.grid(row = 1, column = 1, padx = 10, pady = 10)

root.mainloop() 
