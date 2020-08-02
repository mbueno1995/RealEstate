from django.urls import path
from user import views

urlpatterns = [
    path('social_login',views.social_login,name='social_login'),
]