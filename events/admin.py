from django.contrib import admin
from .models import Event
# Register your models here.
admin.site.register(Event, list_display=['title', 'date', 'location', 'is_active', 'approved'], list_filter=['is_active', 'approved', 'date'])