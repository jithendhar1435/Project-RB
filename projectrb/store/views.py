from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Home page view
def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'categories': categories})

# Category view
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})

# Product detail view
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
