from django.urls import path
from .views import home, category_detail, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
