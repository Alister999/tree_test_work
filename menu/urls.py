from django.urls import path

from menu import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('menu/<slug:menu_slug>/', views.MenuView.as_view(), name='menu'),
    path('phone/', views.phone)
]