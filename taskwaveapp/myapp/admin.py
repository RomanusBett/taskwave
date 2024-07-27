from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_Id', 'recipient', 'subject', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('recipient', 'subject', 'body')
    
    
admin.site.register(Job, JobAdmin)