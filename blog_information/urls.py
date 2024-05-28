from . import views
from django.urls import path

# create your urls here

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
]