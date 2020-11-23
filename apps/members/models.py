from django.db import models
from auditlog.registry import auditlog
from parler.models import TranslatableModel, TranslatedFields
from apps.core.models import (
    AcademicDegree,
    Role,
    Country,
    GraduateProgram,
    Department
)

'''
class Member(models.Model):
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (MAN, 'Male'),
        (WOMAN, 'Female'),
    )
    first_name = models.CharField(max_length = 50, verbose_name = 'First name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last name')
    biography = models.TextField(blank = True, verbose_name = 'Biography')
    sex = models.PositiveIntegerField(choices = SEX_CHOICES, verbose_name = 'Sex')
    birth_date = models.DateField(blank = True, null = True, verbose_name = 'Birthdate')
    email = models.EmailField(max_length = 80, blank = True, verbose_name = 'E-mail')
    phone = models.CharField(max_length = 150, blank = True, verbose_name = 'Phone')
    lattes = models.URLField(max_length = 150, blank = True, verbose_name = 'Lattes link')
    linkedin = models.URLField(max_length = 150, blank = True, verbose_name = 'LinkedIn link')
    orcid = models.URLField(max_length = 150, blank = True, verbose_name = 'ORCID link')
    researchgate = models.URLField(max_length = 150, blank = True, verbose_name = 'Research Gate link')
    address = models.CharField(max_length = 250, blank = True, verbose_name = 'Address')
    image = models.ImageField(upload_to = "members", verbose_name = "Photo", help_text = 'Please, the photo has to be square, e.g. 500x500')
    degree = models.ForeignKey(to = AcademicDegree, on_delete = models.CASCADE, verbose_name = 'Academic degree')
    role = models.ForeignKey(to = Role, on_delete = models.CASCADE, verbose_name = 'Role')
    graduateprogram = models.ForeignKey(to = GraduateProgram, on_delete = models.CASCADE, verbose_name = 'Graduate program')
    department = models.ForeignKey(to = Department, on_delete = models.CASCADE, verbose_name = 'Department')
    country = models.ForeignKey(to = Country, on_delete = models.CASCADE, verbose_name = 'Country')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ["first_name"]

    def __str__(self):
        return "{first_name} {last_name}".format(
                    first_name = self.first_name,
                    last_name = self.last_name
                )
'''

class Member(TranslatableModel):
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (MAN, 'Male'),
        (WOMAN, 'Female'),
    )
    translations = TranslatedFields (
        biography = models.TextField(blank = True, verbose_name = 'Biography')
    )
    first_name = models.CharField(max_length = 50, verbose_name = 'First name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last name')
    sex = models.PositiveIntegerField(choices = SEX_CHOICES, verbose_name = 'Sex')
    birth_date = models.DateField(blank = True, null = True, verbose_name = 'Birthdate')
    email = models.EmailField(max_length = 80, blank = True, verbose_name = 'E-mail')
    phone = models.CharField(max_length = 150, blank = True, verbose_name = 'Phone')
    lattes = models.URLField(max_length = 150, blank = True, verbose_name = 'Lattes link')
    linkedin = models.URLField(max_length = 150, blank = True, verbose_name = 'LinkedIn link')
    orcid = models.URLField(max_length = 150, blank = True, verbose_name = 'ORCID link')
    researchgate = models.URLField(max_length = 150, blank = True, verbose_name = 'Research Gate link')
    address = models.CharField(max_length = 250, blank = True, verbose_name = 'Address')
    image = models.ImageField(upload_to = "members", verbose_name = "Photo", help_text = 'Please, the photo has to be square, e.g. 500x500')
    degree = models.ForeignKey(to = AcademicDegree, on_delete = models.CASCADE, verbose_name = 'Academic degree')
    role = models.ForeignKey(to = Role, on_delete = models.CASCADE, verbose_name = 'Role')
    graduateprogram = models.ForeignKey(to = GraduateProgram, on_delete = models.CASCADE, verbose_name = 'Graduate program')
    department = models.ForeignKey(to = Department, on_delete = models.CASCADE, verbose_name = 'Department')
    country = models.ForeignKey(to = Country, on_delete = models.CASCADE, verbose_name = 'Country')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        # ordering = ["first_name"]

    def __str__(self):
        return "{first_name} {last_name}".format(
                    first_name = self.first_name,
                    last_name = self.last_name
                )

auditlog.register(Member)
