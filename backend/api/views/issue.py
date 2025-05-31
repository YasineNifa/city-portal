from rest_framework import viewsets

from api.models import Issue
from api.serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # permission_classes
