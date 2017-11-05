from django.contrib import admin

from .models import SendgridEvent


admin.site.register(SendgridEvent, list_display=["kind", "email", "created_at"], list_filter=["created_at", "kind"], search_fields=["email", "data"])
