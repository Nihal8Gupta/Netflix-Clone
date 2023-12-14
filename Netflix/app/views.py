from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def movie(request):
    return render(request,'movie.html')

def my_list(request):
    return render(request,'my_list.html')

def search(request):
    return render(request,'search.html')

def genre(request):
    return render(request,'genre.html')