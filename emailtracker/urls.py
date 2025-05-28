from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_email, name='track_email'),
]
