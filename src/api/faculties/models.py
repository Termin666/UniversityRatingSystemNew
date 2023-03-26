from django.db import models
from django.utils.translation import gettext_lazy as _
from api.users.models import CustomUser


class Faculty(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255, unique=True)
    head = models.OneToOneField(verbose_name=_('head'), to=CustomUser, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('faculty')
        verbose_name_plural = _('faculties')

    def __str__(self) -> str:
        return self.name
