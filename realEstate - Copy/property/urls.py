from django.urls import path
from property import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('display_details/<propertyID>/', views.display_details, name='display_details'),
    path('email/<to_email>/', views.email, name='email'),
    path('sendemail', views.sendemail, name='sendemail')
]