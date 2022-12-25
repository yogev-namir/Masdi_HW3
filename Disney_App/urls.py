from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('query_results', views.query_results, name='query_results'),
    path('add_a_movie', views.add_a_movie, name='add_a_movie'),

]