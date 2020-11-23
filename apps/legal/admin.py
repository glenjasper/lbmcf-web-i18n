from django.contrib import admin
from .models import Legal
from parler.admin import TranslatableAdmin

'''
class LegalAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('css/custom_ckeditor.css',)
        }

admin.site.register(Legal, LegalAdmin)
'''

@admin.register(Legal)
class LegalAdmin(TranslatableAdmin):
    list_display = [
        'title',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('css/custom_ckeditor.css',)
        }
