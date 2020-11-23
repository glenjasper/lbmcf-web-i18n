from django.contrib import admin
from .models import Member
from parler.admin import TranslatableAdmin

'''
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'degree',
        'role',
        'graduateprogram',
        'country',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Member, MemberAdmin)
'''

@admin.register(Member)
class MemberAdmin(TranslatableAdmin):
    list_display = [
        '__str__',
        'degree',
        'role',
        'graduateprogram',
        'country',
        'status',
    ]
    readonly_fields = ['created', 'updated']
