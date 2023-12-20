from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email alrady taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username alrady taken')
                return redirect('/signup')
            else:
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/')
                # log user 
                user_login = authenticate()
                
        else:
            messages.info(request,'Password is Not Matching')
            return redirect('/signup')
        
    else:
        return render(request,'signup.html')


def movie(request):
    return render(request,'movie.html')

def my_list(request):
    return render(request,'my_list.html')

def search(request):
    return render(request,'search.html')

def genre(request):
    return render(request,'genre.html')