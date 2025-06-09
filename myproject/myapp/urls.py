from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                
    path('products/', views.products, name='products'),
    path('working/', views.working, name='working'),   
    path('polos/', views.polos, name='polos'),
    path('tshirts/', views.tshirts, name='tshirts'),
    path('jackets/', views.jackets, name='jackets'),
    path('sweatshirts/', views.sweatshirts, name='sweatshirts'),
    path('hoodie/', views.hoodie, name='hoodie'),
    path('about/',views.about,name='about'),
    # path('hoodies_detail/',views.hoodies_detail,name='hoodies_detail'),
     path('hoodie/<int:hoodie_id>/', views.hoodie_detail, name='hoodie_detail'),

     

]



