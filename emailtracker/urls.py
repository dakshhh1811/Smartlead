from django.urls import path
from .views import track_email_event

urlpatterns = [
    path('track/', track_email_event, name='track_email_event'),
]
