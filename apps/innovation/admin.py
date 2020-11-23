from django.contrib import admin
from .models import (
    Patent,
)

class PatentAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'register_number',
        'patent_type',
        'registry_institution',
        'deposit_date',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    ordering = ['title', 'patent_type', 'registry_institution']
    date_hierarchy = 'deposit_date'

admin.site.register(Patent, PatentAdmin)
