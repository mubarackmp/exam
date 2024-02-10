from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app1.models import *
from app1.form import *
# Create your views here.
def index(request):
    a= product.objects.all()
    b=catogory.objects.all()
    return render(request,'index.html',{'p':a, 'c':b})


def shop(request, p_id):
    d=catogory.objects.all()
    a= catogory.objects.get(id=p_id)
    b= product.objects.filter(catogory=a)
    return render(request,'shop.html',{'f':b, 'm':d})

def add(request):
    a=productForm()
    if request.method == 'POST':
        a=productForm(request.POST,request.FILES)
        if a.is_valid():
            a.save()
    return render(request,'addproduct.html',{'form':a})

def deletey(request, dele):
    a = product.objects.get(id =dele)
    a.delete()
    return redirect('app1:home')


def showcart(request):
    cart_item = cartu.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.contity for item in cart_item)
    return render(request,'cart.html',{'c':cart_item, 'total':total_price})


def addtocart(request, prod_id):
    prod = product.objects.get(id=prod_id)
    cartu_item, created = cartu.objects.get_or_create(product=prod, user=request.user)
    cartu_item.contity +=1
    cartu_item.save()
    return redirect('app1:cart')

def removecart(request,item_id):
    cart_item = cartu.objects.filter(id=item_id)
    cart_item.delete()
    return redirect('app1:cart')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        ps1 = request.POST.get('pass1')
        user = authenticate(username=username,password=ps1)
        if user is not None:
            login(request, user)
            return redirect('app1:home')
        else:
            print('wrong password of username')
            return redirect('app1:logine')

    return render(request,'login.html')


def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        ps1 = request.POST.get('pass1')
        ps2 = request.POST.get('pass2')
        if ps1==ps2:
            if User.objects.filter(username=username,email=email).exists():
                print('already have')
                return redirect('app1:signupe')
            else:
                new_user = User.objects.create_user(username,email,ps1)
                new_user.save()
                return redirect('app1:logine')
        else:
            print('password missmatch')
        
    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('app1:logine')

