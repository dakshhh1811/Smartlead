from django.db import models

class EmailEvent(models.Model):
    email = models.EmailField()
    event_type = models.CharField(max_length=50)
    campaign_id = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.event_type} at {self.timestamp}"
