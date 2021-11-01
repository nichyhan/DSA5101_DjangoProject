from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie, name='movie'),
    path('movies/sortbyname/', views.sortbyname, name='sortbyname'),
    # Add paths which link to view.py
    # 1) sort by duration
    # 2) sort by date released

    path('movies/filter/', views.filter, name='moviefilter'),



]