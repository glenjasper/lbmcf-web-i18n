from django.contrib import admin
from .models import (
    Partnership,
)

class PartnershipAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'country',
        'institution',
        'get_state',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    ordering = ['country', 'institution', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'country__name', 'institution__full_name', 'institution__state__name']

    def get_state(self, obj):
        return obj.institution.state
    get_state.short_description = 'State'

admin.site.register(Partnership, PartnershipAdmin)
