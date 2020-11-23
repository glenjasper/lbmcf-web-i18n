from django.db import models
from ckeditor.fields import RichTextField
from auditlog.registry import auditlog
from parler.models import TranslatableModel, TranslatedFields

'''
class Legal(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Title')
    # content = models.TextField(verbose_name = 'Content')
    content = RichTextField(verbose_name = 'Content')
    order = models.SmallIntegerField(verbose_name = 'Order', default = 0)
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Legal"
        verbose_name_plural = "Legal"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
'''

class Legal(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(max_length = 200, verbose_name = 'Title'),
        # content = models.TextField(verbose_name = 'Content'),
        content = RichTextField(verbose_name = 'Content')
    )
    order = models.SmallIntegerField(verbose_name = 'Order', default = 0)
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Legal"
        verbose_name_plural = "Legal"
        ordering = ["order"]

    def __str__(self):
        return self.title

auditlog.register(Legal)
