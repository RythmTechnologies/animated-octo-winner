from django.contrib import admin
from .models import LogEntry
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'description', 'timestamp', 'content_type')
    list_filter = ('action', 'timestamp',)
    
    def has_add_permission(self, request, obj=None):
        # LogEntry kayıtlarının admin paneli üzerinden eklenmesini engelle
        return False

    def has_change_permission(self, request, obj=None):
        # LogEntry kayıtlarının admin paneli üzerinden değiştirilmesini engelle
        return False

