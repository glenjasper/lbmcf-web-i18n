from django.contrib import admin
from .models import (
    Link
)

class LinkAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'link',
        'logo',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Link, LinkAdmin)
