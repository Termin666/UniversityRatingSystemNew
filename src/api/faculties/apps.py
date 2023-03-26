from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FacultiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.faculties'
    verbose_name = _('faculties')
