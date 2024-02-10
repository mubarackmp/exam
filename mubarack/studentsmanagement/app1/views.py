from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')


def add(request):
    return render(request,'adddetails.html')



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

def show(request):
    return request(request,'studentsdetails.html')