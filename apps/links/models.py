from django.db import models
from auditlog.registry import auditlog

class Link(models.Model):
    name = models.CharField(max_length = 150, verbose_name = 'Name')
    link = models.URLField(max_length = 150, verbose_name = 'Link')
    logo = models.ImageField(upload_to = "links", verbose_name = "Logo image")
    order = models.SmallIntegerField(verbose_name = 'Order', default = 0)
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

auditlog.register(Link)
