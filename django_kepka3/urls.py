"""django_kepka3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from custom_caps import views

#все урлы касательно магазина, производителя, кепок. Урлы юзера в приложении users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/magazine/', views.MagazineListAPIview.as_view()),
    path('api/v1/magazine/<int:id>/', views.MagazineItemUpdateDeleteAPIview.as_view()),
    path('api/v1/manufacturer/', views.ManufacturerListAPIview.as_view()),
    path('api/v1/manufacturer/<int:id>/', views.ManufacturerItemUpdateDeleteAPIview.as_view()),
    path('api/v1/caps/', views.CapsListAPIview.as_view()),
    path('api/v1/caps/<int:id>/', views.CapsItemUpdateDeleteAPIview.as_view()),
    path('api/v1/category/', views.CategoryListAPIview.as_view()),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/discounts/', include('discounts.urls'))
]
