from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    AcademicDegree,
    Financer,
    Country,
    State,
    Institution,
    Department,
    Role,
    GraduateProgram,
    ProtocolType,
    FileType,
    RegistryInstitution,
    PatentType
)

'''
class FinancerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class AcademicDegreeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'image',
        'status'
    ]
    readonly_fields = ['created', 'updated']
    ordering = ['name']
    search_fields = ['name', 'code']

class InstitutionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'country',
        'state',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    ordering = ['full_name']
    search_fields = ['name', 'full_name', 'country__name', 'state__name']
    # list_filter = ['country__name, state__name']

class GraduateProgramAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'institution',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class ProtocolTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class FileTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class RegistryInstitutionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'full_name',
        'country',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class PatentTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Financer, FinancerAdmin)
admin.site.register(AcademicDegree, AcademicDegreeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(GraduateProgram, GraduateProgramAdmin)
admin.site.register(ProtocolType, ProtocolTypeAdmin)
admin.site.register(FileType, FileTypeAdmin)
admin.site.register(RegistryInstitution, RegistryInstitutionAdmin)
admin.site.register(PatentType, PatentTypeAdmin)
'''

@admin.register(Financer)
class FinancerAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'full_name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(AcademicDegree)
class AcademicDegreeAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'description',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(Role)
class RoleAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(Department)
class DepartmentAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'full_name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'image',
        'status'
    ]
    readonly_fields = ['created', 'updated']
    ordering = ['name']
    search_fields = ['name', 'code']

@admin.register(Institution)
class InstitutionAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'full_name',
        'country',
        'state',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    # ordering = ['full_name']
    search_fields = ['name', 'full_name', 'country__name', 'state__name']
    # list_filter = ['country__name, state__name']

@admin.register(GraduateProgram)
class GraduateProgramAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'full_name',
        'institution',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(ProtocolType)
class ProtocolTypeAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(FileType)
class FileTypeAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(RegistryInstitution)
class RegistryInstitutionAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'full_name',
        'country',
        'status',
    ]
    readonly_fields = ['created', 'updated']

@admin.register(PatentType)
class PatentTypeAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
