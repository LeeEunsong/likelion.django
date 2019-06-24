from django.urls import path, include
from . import views

urlpatterns = [
    
    path('signup/', views.sigup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('logout/',views.logout, name="logout"),
] 