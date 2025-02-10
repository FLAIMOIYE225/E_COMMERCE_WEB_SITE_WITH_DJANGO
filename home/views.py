from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from store.models import Product, Category


# Create your views here.
def index(request):

    user = get_user(request)

    categors = Category.objects.all()
    lastest_products = Product.objects.all()[:8]
    featuredProducts = Product.objects.all().order_by('-rating')[:4]

    return render(request, 'home/index.html', context={'products' : lastest_products, 'categorys' : categors, 'featuredProducts':featuredProducts})