from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    News,
    EventPhoto
)

class EventPhotoInline(admin.TabularInline):
    model = EventPhoto

    def get_extra(self, request, obj=None, **kwargs):
        extra = 10
        if obj:
            return extra - obj.eventphoto_set.count()
        return extra

    '''
    # Número máximo de items a agregar
    def get_max_num(self, request, obj = None, **kwargs):
        max_num = 15
        if obj and obj.parent:
            return max_num - 5
        return max_num
    '''

'''
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date',
        'logo',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    inlines = [
        EventPhotoInline,
    ]

admin.site.register(News, NewsAdmin)
'''

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = [
        'title',
        'date',
        'logo',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    inlines = [
        EventPhotoInline,
    ]
