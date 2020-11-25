from django.contrib import admin
from .models import Controller
from parler.admin import TranslatableAdmin

'''
@admin.register(Controller)
class ControllerAdmin(TranslatableAdmin):
    list_display = [
        'id',
        'name',
        'enabler',
    ]
    readonly_fields = ['created', 'updated']
'''

class ControllerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'enabler',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Controller, ControllerAdmin)
