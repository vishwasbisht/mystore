from django.db import models
from django.contrib.auth.models import User

# class Customer(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     email = models.CharField(max_length=100, null=False)
#     phone = models.CharField(max_length=100, null=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name.title()


# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     description = models.TextField(max_length=1000, null=True)
#     image = models.ImageField(null=True, blank=True)
#     isactive = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name.title()
    
#     @property
#     def imageurl(self) :
#         try :
#             url = self.image.url
#         except :
#             url = "/images/placeholder.png"   
#             return url 
        
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     orderdate = models.DateTimeField(auto_now_add=True)
#     transaction_id = models.CharField(max_length=200, null=True)
#     complete = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.id)


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     date_added = models.DateTimeField(auto_now_add=True)
    
    
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     address = models.CharField(max_length=500)
#     city = models.CharField(max_length=500)
#     state = models.CharField(max_length=500)
#     zipcode = models.CharField(max_length=500)

#     def __str__(self):
#         return self.address
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name.title()

    @property
    def imageurl(self):
        try:
            return self.image.url
        except (ValueError, AttributeError):
            return '/images/placeholder.png'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"
    
    @property 
    def get_cart_total(self) :
        orderitems = self.orderitem_set.all()
        return sum([item.get_total for item in orderitems] )
    
    def get_cart_items(self) :
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])
        
        


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    @property
    def get_total(self) :
        return self.product.price * self.quantity
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}" 