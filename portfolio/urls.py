from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"), #portfolio 중복으로 앞쪽 지움
]