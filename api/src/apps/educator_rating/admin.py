from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (EducatorIndicatorValue, EducatorRatingPartition,
                     EducatorReport, EducatorReportController)


@admin.register(EducatorRatingPartition)
class EducatorRatingPartitionAdmin(admin.ModelAdmin):
    list_display = ('partition', )
    autocomplete_fields = ('partition', )


@admin.register(EducatorIndicatorValue)
class EducatorIndicatorValueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'report', 'indicator', )
    autocomplete_fields = ('report', 'indicator', )


@admin.register(EducatorReport)
class EducatorReportAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'year', 'approved', )
    search_fields = (
        'educator__user__first_name', 'educator__user__last_name',
        'educator__user__patronymic',
    )
    list_select_related = ('educator__user', 'educator__qualification')
    search_help_text = _('Educator first name, lastname or patronymic')
    list_filter = ('educator__qualification__name', 'year', )
    autocomplete_fields = ('educator', )
    exclude = ('approved', )


@admin.register(EducatorReportController)
class EducatorReportControllerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', )
    search_fields = (
        'user__email', 'user__first_name', 'user__last_name',
        'user__patronymic', 'department__name',
    )
    search_help_text = _(
        ('Department name or controller email, '
         'first name, last name or patronymic')
    )
    autocomplete_fields = ('user', 'department', )
