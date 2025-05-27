from django.db import models

class EmailEvent(models.Model):
    email_id = models.EmailField()
    event_type = models.CharField(max_length=50)  # opened, clicked, bounced, etc.
    timestamp = models.DateTimeField()
    campaign_id = models.CharField(max_length=100)
    received_at = models.DateTimeField(auto_now_add=True)
