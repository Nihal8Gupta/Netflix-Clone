from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('search/',search,name='search'),
    path('my_list/',my_list,name='my_list'),
    path('movie/',movie,name='movie'),
    path('genre/',genre,name='genre'),
]