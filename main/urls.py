from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a-propos/', views.about, name='about'),
    path('technologie-projets/', views.technology, name='technology'),
    path('impact/', views.impact, name='impact'),
    path('contact/', views.contact, name='contact'),
]