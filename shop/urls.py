from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('review_product/<int:product_id>/', views.review_product,
         name='review_product'),
]
