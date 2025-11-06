from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')