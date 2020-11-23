from django.contrib import admin
from .models import (
    Paper
)

class PaperAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'published',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    ordering = ['title', 'published']
    search_fields = ['title', 'keywords', 'abstract', 'authors'] # author__name
    date_hierarchy = 'published'
    # list_filter = ['authors'] # author__name

    '''
    def all_authors(self, obj):
        return ", ".join([c.name for c in obj.authors.all().order_by("name")])
    all_authors.short_description = 'Authors'
    '''
    '''
    fieldsets = [
        ('Movie information',    {'fields': ['name', 'synopsis', 'release_date', 'rate_count', 'rate', 'image']}),
        ('Tag information',      {'fields': ['tags']}),
        ('Studio information',   {'fields': ['studio']}),
        ('Director information', {'fields': ['director'], 'classes': ['collapse']}),
    ]
    exclude = ['created', 'updated']
    '''

admin.site.register(Paper, PaperAdmin)
