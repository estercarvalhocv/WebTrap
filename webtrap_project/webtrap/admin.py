from django.contrib import admin
from .models import RequestLog, HoneypotSubmission

class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('method', 'url', 'timestamp')
    search_fields = ('url',)

class HoneypotSubmissionAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'timestamp')
    search_fields = ('nome', 'email')

admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(HoneypotSubmission, HoneypotSubmissionAdmin)