from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/app/login/')
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    
    return render(request,'index.html',context)


def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None: 
            auth.login(request,user)
            return redirect('/app/index')
        else:
            messages.info(request,'Credentials Invalid !!')
            return redirect('/app/login')
    return render(request,'login.html')

@login_required(login_url='/app/login/')
def movie(request,pk):
    movie_uuid = pk
    movie_details = Movie.objects.get(uu_id=movie_uuid)
    context = {'movie_details':movie_details}

    return render(request,'movie.html',context)


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email alrady taken')
                return redirect('/app/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username alrady taken')
                return redirect('/app/signup')
            else:
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                
                return redirect('/app/')
                
        else:
            messages.info(request,'Password is Not Matching')
            return redirect('/app/signup')
        
    else:
        return render(request,'signup.html')




def my_list(request):
    return render(request,'my_list.html')

def search(request):
    return render(request,'search.html')

def genre(request):
    return render(request,'genre.html')