from django.urls import path, include
from .views import home,cart,checkout,updatecart,product_detail

urlpatterns = [
    path('', home, name="store"),
    path('product/<int:pk>/', product_detail, name="product_detail"),
    path('cart/', cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path('update_item/', updatecart, name="updatecart"),
    
  
 
]