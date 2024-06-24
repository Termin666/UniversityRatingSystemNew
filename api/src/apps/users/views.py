from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import AllowedEmail
from .serializers import AllowedEmailSerializer

from django.http import HttpResponse
from ..create_pdf import create_pdf
import os

from ..educator_rating.models import EducatorReport
from ..integration_1c.convertions import bundle_report


def generate_pdf(request, user_id):
    report = EducatorReport.objects.get(id=user_id)
    data = bundle_report(report)

    pdf_path = create_pdf(data['employeeId'], data['year'], data)
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'
        return response

class AllowedEmailViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = AllowedEmail.objects.all().order_by('pk')
    serializer_class = AllowedEmailSerializer
    permission_classes = (IsAdminUser, )



