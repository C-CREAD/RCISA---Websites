from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location', 'created_at')
    search_fields = ('title', 'description', 'location')
    list_filter = ('start_time', 'location')
    readonly_fields = ('slug', 'created_at', 'updated_at')


admin.site.register(Event, EventAdmin)