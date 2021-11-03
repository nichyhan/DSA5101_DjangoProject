from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie, name='movie'),
    path('movies/sortbyname/', views.sortbyname, name='sortbyname'),
    path('movies/durationascending/', views.durationascending, name='durationascending'),
    path('movies/durationdecending/', views.durationdecending, name='durationdecending'),
    path('movies/sortbyreleased/', views.sortbyreleased, name='sortbyreleased'),

    path('movies/filter/', views.filter, name='filter'),

]