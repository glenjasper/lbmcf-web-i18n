from django.db import models
from django.utils.timezone import now
from auditlog.registry import auditlog

class Paper(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Title')
    abstract = models.TextField(verbose_name = 'Abstract')
    keywords = models.CharField(max_length = 300, blank = True, verbose_name = 'Key words')
    authors = models.TextField(verbose_name = 'Authors')
    published = models.DateField(verbose_name = 'Publication date', default = now)
    doi = models.URLField(max_length = 200, verbose_name = 'DOI', help_text = 'Digital Object Identifier')
    pdf = models.FileField(upload_to = 'publications', blank = True, verbose_name = 'Pdf', help_text = 'Pdf file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Paper"
        verbose_name_plural = "Papers"
        ordering = ["-published"]

    def __str__(self):
        return self.title

auditlog.register(Paper)
