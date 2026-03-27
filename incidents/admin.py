from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')