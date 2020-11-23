from django.db import models
from auditlog.registry import auditlog
from parler.models import TranslatableModel, TranslatedFields

'''
class News(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    location = models.CharField(max_length = 250, verbose_name = 'Location', help_text = 'Place of the event')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description of the event')
    link = models.URLField(max_length = 150, blank = True, verbose_name = 'Event link')
    date = models.DateField(verbose_name = 'Date', help_text = 'Date of the event')
    logo = models.ImageField(upload_to = 'news', verbose_name = 'Logo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-date"]

    def __str__(self):
        return self.title
'''

class News(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(max_length = 80, verbose_name = 'Title'),
        location = models.CharField(max_length = 250, verbose_name = 'Location', help_text = 'Place of the event'),
        description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description of the event')
    )
    link = models.URLField(max_length = 150, blank = True, verbose_name = 'Event link')
    date = models.DateField(verbose_name = 'Date', help_text = 'Date of the event')
    logo = models.ImageField(upload_to = 'news', verbose_name = 'Logo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-date"]

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    news = models.ForeignKey(to = News, on_delete = models.CASCADE, verbose_name = 'News')
    photo = models.ImageField(upload_to = 'news', verbose_name = 'Photo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "EventPhoto"
        verbose_name_plural = "EventPhotos"
        ordering = ["photo"]

    # def __str__(self):
    #    return self.photo

auditlog.register(News)
auditlog.register(EventPhoto)
