from django.urls import path

from menu import views

urlpatterns = [
    path('', views.MainView.as_view())
]