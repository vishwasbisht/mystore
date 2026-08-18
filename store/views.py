
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Customer, Order, OrderItem

# 1. Store Home View
def home(request):
    prds = Product.objects.filter(isactive=True).order_by("price")
    
    # Pass order to context so base.html navbar cart badge works
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(
            user=request.user, 
            defaults={'name': request.user.username, 'email': request.user.email}
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    data = {"prds": prds, "order": order}
    return render(request, "store/home.html", data)

# 2. Cart View
def cart(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(
            user=request.user, 
            defaults={'name': request.user.username, 'email': request.user.email}
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, "store/cart.html", context)

# 3. Checkout View
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    customer, created = Customer.objects.get_or_create(
        user=request.user, 
        defaults={'name': request.user.username, 'email': request.user.email}
    )
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {'items': items, 'order': order}
    return render(request, "store/checkout.html", context)

# 4. Backend Update Cart View (handles pure HTML POST form submissions)
@login_required(login_url='login')
def updatecart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action', 'add')
        
        customer, created = Customer.objects.get_or_create(
            user=request.user, 
            defaults={'name': request.user.username, 'email': request.user.email}
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        product = get_object_or_404(Product, id=product_id)
        
        # Check 'created' boolean from get_or_create
        order_item, item_created = OrderItem.objects.get_or_create(
            order=order, 
            product=product,
            defaults={'quantity': 1} # Sets default to 1 on creation
        )
        
        # Only increment if the item ALREADY existed before this click
        if not item_created:
            if action == 'add':
                order_item.quantity += 1
            elif action == 'remove':
                order_item.quantity -= 1
        elif action == 'remove':
            order_item.quantity -= 1

        order_item.save()
        
        if order_item.quantity <= 0 or action == 'delete':
            order_item.delete()

        return redirect('cart')

    return redirect('home')

# 5. Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(
            user=request.user, 
            defaults={'name': request.user.username, 'email': request.user.email}
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {"product": product, "order": order}
    return render(request, "store/product_detail.html", context)
    
    

