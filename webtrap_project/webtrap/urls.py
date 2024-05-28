from django.urls import path
from . import views

urlpatterns = [
    path('honeypot/', views.honeypot, name='honeypot'),
    path('honeypot-form/', views.honeypot_form, name='honeypot_form'),
]
