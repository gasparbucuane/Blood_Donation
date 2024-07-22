from . import views
from django.urls import path

urlpatterns = [
    path('', views.donor_create, name = 'donor_create'),
    path('list_donations/', views.list_donations, name ='list_donation'),
    path('donor_info/<str:id>', views.donor_info, name = 'donor_info'),
    path('home/', views.home, name = 'home'),
]

