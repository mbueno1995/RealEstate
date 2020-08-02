from django.urls import path, include
from property import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('properties', views.PropertyViewSet)

urlpatterns = [path('display_details/<propertyID>/', views.display_details, name='display_details'),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),

    path('email/<to_email>/', views.email, name='email'),
    path('sendemail', views.sendemail, name='sendemail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('googlenews', views.googlenews, name='googlenews'),
    path('weathernews', views.weathernews, name='weathernews'),

    path('', include(router.urls)),
]