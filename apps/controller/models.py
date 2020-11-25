from django.db import models
from django.utils.timezone import now
from auditlog.registry import auditlog
from parler.models import TranslatableModel, TranslatedFields

'''
class Controller(TranslatableModel):
    translations = TranslatedFields (
        name = models.CharField(max_length = 100, verbose_name = 'Name')
    )
    enabler = models.BooleanField(default = True, verbose_name =  'Enabler')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Controller"
        verbose_name_plural = "Controllers"
        # ordering = ["name"]

    def __str__(self):
        return self.name
'''

class Controller(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Name')
    enabler = models.BooleanField(default = True, verbose_name =  'Enabler')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Controller"
        verbose_name_plural = "Controllers"
        ordering = ["name"]

    def __str__(self):
        return self.name

auditlog.register(Controller)
