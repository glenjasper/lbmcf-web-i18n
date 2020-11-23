from django.db import models
from auditlog.registry import auditlog
from apps.core.models import Financer, ProtocolType, FileType
from parler.models import TranslatableModel, TranslatedFields

'''
class Project(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Project name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Project summary')
    financer = models.ForeignKey(to = Financer, on_delete = models.CASCADE, verbose_name = 'Financer name')
    date = models.DateField(help_text = 'project start date', verbose_name = 'Start date')
    image = models.ImageField(upload_to = 'projects', verbose_name = "Reference image")
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date"]

    def __str__(self):
        return self.title

class Protocol(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    type = models.ForeignKey(to = ProtocolType, on_delete = models.CASCADE, verbose_name = 'Type')
    pdf = models.FileField(upload_to = 'protocols', verbose_name = 'Doc, Docx, Xls, Xlsx, Pdf', help_text = 'Protocol file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Protocol"
        verbose_name_plural = "Protocols"
        ordering = ["name"]

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    type = models.ForeignKey(to = FileType, on_delete = models.CASCADE, verbose_name = 'Type')
    pdf = models.FileField(upload_to = 'files', verbose_name = 'Doc, Docx, Xls, Xlsx, Pdf', help_text = 'File file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = ["name"]

    def __str__(self):
        return self.name
'''

class Project(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(max_length = 300, verbose_name = 'Project name'),
        description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Project summary')
    )
    financer = models.ForeignKey(to = Financer, on_delete = models.CASCADE, verbose_name = 'Financer name')
    date = models.DateField(help_text = 'project start date', verbose_name = 'Start date')
    image = models.ImageField(upload_to = 'projects', verbose_name = "Reference image")
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date"]

    def __str__(self):
        return self.title

class Protocol(TranslatableModel):
    translations = TranslatedFields (
        name = models.CharField(max_length = 200, verbose_name = 'Name'),
        description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    )
    type = models.ForeignKey(to = ProtocolType, on_delete = models.CASCADE, verbose_name = 'Type')
    pdf = models.FileField(upload_to = 'protocols', verbose_name = 'Doc, Docx, Xls, Xlsx, Pdf', help_text = 'Protocol file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Protocol"
        verbose_name_plural = "Protocols"
        # ordering = ["name"]

    def __str__(self):
        return self.name

class File(TranslatableModel):
    translations = TranslatedFields (
        name = models.CharField(max_length = 200, verbose_name = 'Name'),
        description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    )
    type = models.ForeignKey(to = FileType, on_delete = models.CASCADE, verbose_name = 'Type')
    pdf = models.FileField(upload_to = 'files', verbose_name = 'Doc, Docx, Xls, Xlsx, Pdf', help_text = 'File file')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        # ordering = ["name"]

    def __str__(self):
        return self.name

auditlog.register(Project)
auditlog.register(Protocol)
auditlog.register(File)
