from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('product', views.product, name='product'),
    path('support', views.support, name='support'),
    path('price', views.price, name='price'),
    path('cart', views.cart, name='cart'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login',views.user_login, name='login'),
    path('register', views.register, name='register'),

]