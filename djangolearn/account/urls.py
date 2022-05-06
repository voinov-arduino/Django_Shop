from django.conf.urls import path
from . import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]