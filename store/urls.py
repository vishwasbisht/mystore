from django.urls import path
from . import views

urlpatterns = [
    # Named both 'store' and 'home' so all templates work without errors
    path('', views.home, name='store'),
    path('home/', views.home, name='home'),
    
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_cart/', views.updatecart, name='updatecart'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]