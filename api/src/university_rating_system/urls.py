import os

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from users.views import generate_pdf

urlpatterns = [
    path('', include('apps.core.urls')),
    path('generate-pdf/<int:user_id>/', generate_pdf, name='generate-pdf'),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))

else:
    urlpatterns.append(
        path(
            f'{os.getenv("ADMIN_SITE_URL")}/',
            admin.site.urls
        )
    )
