from django.contrib import admin
from django.urls import path

from sqlquery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('products/', views.products, name='products'),
    path('duplicates/', views.duplicates, name='duplicates'),
    path('', views.html_template, name='html'),
]
