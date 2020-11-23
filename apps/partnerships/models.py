from django.db import models
from auditlog.registry import auditlog
from apps.core.models import (
    AcademicDegree,
    Country,
    Institution
)

class Partnership(models.Model):
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (MAN, 'Male'),
        (WOMAN, 'Female'),
    )
    first_name = models.CharField(max_length = 50, verbose_name = 'First name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last name')
    sex = models.PositiveIntegerField(verbose_name = 'Sex', choices = SEX_CHOICES)
    email = models.EmailField(max_length = 80, blank = True, verbose_name = 'E-mail')
    phone = models.CharField(max_length = 150, blank = True, verbose_name = 'Phone')
    link = models.URLField(max_length = 150, blank = True, verbose_name = 'Link (cv or lattes)')
    degree = models.ForeignKey(to = AcademicDegree, on_delete = models.CASCADE, verbose_name = 'Academic degree')
    institution = models.ForeignKey(to = Institution, on_delete = models.CASCADE, verbose_name = 'Institution')
    country = models.ForeignKey(to = Country, on_delete = models.CASCADE, verbose_name = 'Country')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Partnership"
        verbose_name_plural = "Partnerships"
        ordering = ["first_name"]

    def __str__(self):
        return "{first_name} {last_name}".format(
                    first_name = self.first_name,
                    last_name = self.last_name
                )

auditlog.register(Partnership)
