from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('flight/<int:pk>/', views.flight_detail, name='flight_detail'),
]