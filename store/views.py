# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
# from .models import Product
# # from .forms import UserRegisterForm, CustomerForm

# # Create your views here.

# def home(request):
#     prds = Product.objects.filter(isactive=True).order_by("price")
#     data = {"prds": prds}
#     return render(request, "store/home.html", data)

# def cart(request):
#     data = {}
#     return render(request, "store/cart.html", data)

# def checkout(request):
#     data = {}
#     return render(request, "store/checkout.html", data)



# def updatecart(request):
#     if request.user.is_authenticated == True:
#         return HttpResponse("add to cart")
#     else:
#         return redirect("/auth/login")


# def logout1(request):
#     logout(request)
#     prds = Product.objects.filter(isactive=True).order_by("price")
#     data = {"prds": prds}
#     return render(request, "store/home.html", data)


# def register(request):
#     if request.method == "POST":
#         usr_frm = UserRegisterForm(request.POST)
#         cst_frm = CustomerForm(request.POST)
#         if usr_frm.is_valid() and cst_frm.is_valid():
#             user = usr_frm.save()
#             cst = cst_frm.save(commit=False)
#             cst.user = user
#             cst.save()
#             login(request, user)
#             return redirect("store")
#         else:
#             return redirect("store")
#     else:
#         usr_frm = UserRegisterForm()
#         cst_frm = CustomerForm()
#         data = {"usr_frm": usr_frm, "cst_frm": cst_frm}
#         return render(request, "store/register.html", data)


# Create your views here.

from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.http import JsonResponse
from django.http import HttpResponse

def home(request) :
    prd = Product.objects.filter(isactive=True).order_by("price")
    data = {"prds" : prd}
    return render(request,"store/home.html",data)

def cart(request) :
    data = {}
    return render(request,"store/cart.html",data)

def checkout(request) :
    data = {}
    return render(request,"checkout/cart.html",data)

# def updatecart(request):
#     return JsonResponse({'message': 'Cart updated'}, safe=False)

def updatecart(request):
    if request.user.is_authenticated == True:
        return HttpResponse("add to cart")
    else:
        return redirect("/auth/login")
    
    
def product_detail(request,pk) :
    product = get_object_or_404(Product, id=pk)
    return render(request,"store/product_detail.html",{"product":product})
    
    

