"""jernskegg_art URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from simple_pages import views as pageView
from gallery import views as galleryView
from account import views as AccountView
from commission import views as CommissionView
from cart import views as CartView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pageView.get_home, name='home'),
    path('gallery/', galleryView.ImageList.as_view(), name='gallery'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', AccountView.GetAccount.as_view(), name='account'),
    path('about/', pageView.get_about, name='about'),
    path('commision/', CommissionView.addRequest, name='request'),
    path('cart/', CartView.get_cart, name='cart' )
]
