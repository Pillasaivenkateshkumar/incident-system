from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'severity',
        'location',
        'reported_by',
        'created_at'
    )
    list_filter = ('severity', 'created_at')
    search_fields = ('title', 'description', 'location', 'reported_by')