from django.shortcuts import render
from django.http import HttpResponse
from .models.product import  Product
# Create your views here.


def index(request,):
    products = Product.get_all_products();
    print(products)
    #return render(request, 'orders/order.html')
    return render(request, 'index.html', {'products' : products})