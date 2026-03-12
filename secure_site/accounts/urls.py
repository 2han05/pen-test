from django.urls import path
from .views import register_view, dashboard_view, contact_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('register/', register_view, name='register'),
    path('contact/', contact_view, name='contact'),
]