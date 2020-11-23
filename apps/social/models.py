from django.db import models
from auditlog.registry import auditlog

class LinkSocial(models.Model):
    key = models.SlugField(max_length = 100, unique = True, verbose_name = 'Link key')
    name = models.CharField(max_length = 200, verbose_name = 'Social Network')
    url = models.URLField(max_length = 200, blank = True, null = True, verbose_name = 'Link')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ["name"]

    def __str__(self):
        return self.name

auditlog.register(LinkSocial)
