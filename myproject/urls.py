"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # URL for the home view
    path('signup/', views.signup , name='signup'),  # URL for the signup view
    path('login/', views.login , name='login'),  # URL for the login view
    path('about/', views.about, name='about'),  # URL for the about view
    path('contact/', views.contact, name='contact'),  # URL for the contact view
    path('cart/', views.cart, name='cart'),  # URL for the cart view
    path('product/', views.product, name='product'),  # URL for the product view
    path('product2/', views.product2, name='product2'),  # URL for the product2 view
    path('product3/', views.product3, name='product3'),  # URL for the product3 view
    path('product4/', views.product4, name='product4'),  # URL for the product4 view
    path('product5/', views.product5, name='product5'),  # URL for the product5 view
    path('shop/', views.shop, name='shop'),  # URL for the shop view
    path('shops/', views.shops, name='shops'),  # URL for the shops view

]

