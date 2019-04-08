"""Elite_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from User_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^user_app/', include("User_app.urls")),
    url(r'^index/', views.index, name="index"),
    url(r'^busi/', views.business, name="business"),
    url(r'^ent/', views.entertainment, name="entertainment"),
    url(r'^life/', views.lifestyle, name="lifestyle"),
    url(r'^login/', views.login, name="login"),
    url(r'^reg/', views.register, name="register"),
    url(r'^sports/', views.sports, name="sports"),
    url(r'^tech/', views.technology, name="technology"),
    url(r'^world/', views.world, name="world"),
]
