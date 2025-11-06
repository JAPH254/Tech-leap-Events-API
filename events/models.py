from django.db import models
from auth_users.models import CustomUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    isOrganizer = models.BooleanField(default=False)
    isAttendee = models.BooleanField(default=True)
    RSVP_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title