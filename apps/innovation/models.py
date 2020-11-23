from django.db import models
from apps.core.models import RegistryInstitution, PatentType
from django.utils.timezone import now
from auditlog.registry import auditlog

class Patent(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Title')
    authors = models.TextField(verbose_name = 'Authors')
    abstract = models.TextField(blank = True, verbose_name = 'Abstract')
    register_number = models.CharField(max_length = 100, verbose_name = 'Register number')
    deposit_date = models.DateField(verbose_name = 'Deposit date', default = now)
    patent_type = models.ForeignKey(to = PatentType, on_delete = models.CASCADE, verbose_name = 'Patent type')
    registry_institution = models.ForeignKey(to = RegistryInstitution, on_delete = models.CASCADE, verbose_name = 'Registry institution')
    url = models.URLField(max_length = 200, blank = True, verbose_name = 'URL', help_text = 'Patent link')
    # pdf = models.FileField(upload_to = 'patents', blank = True, verbose_name = 'Pdf', help_text = 'Pdf file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Patent"
        verbose_name_plural = "Patents"
        ordering = ["-deposit_date"]

    def __str__(self):
        return self.title

auditlog.register(Patent)
