from django.conf.urls import url
from User_app import views
app_name = "User_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^busi/', views.index, name="business"),
    url(r'^ent/', views.index, name="entertainment"),
    url(r'^life/', views.index, name="lifestyle"),
    url(r'^login/', views.index, name="login"),
    url(r'^reg/', views.index, name="register"),
    url(r'^sports', views.index, name="sports"),
    url(r'^tech', views.index, name="technology"),
    url(r'^world', views.index, name="world"),

]
