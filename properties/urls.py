from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<slug:slug>/', views.property_detail, name='property_detail'),
    path('<slug:slug>/save/', views.toggle_save_property, name='toggle_save_property'),
]
