from django.urls import path
from backend import views

urlpatterns = [
    path('', views.call_default, name="home"),
    path('last_15M/', views.call_last_15, name="last_15"),
    path('last_1H/', views.call_last_1, name="last_1"),
    path('last_4H/', views.call_last_4, name="last_4"),
]