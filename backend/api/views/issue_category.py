from rest_framework import viewsets

from api.models import IssueCategory
from api.serializers import IssueCategorySerializer


class IssueCategoryViewSet(viewsets.ModelViewSet):
    queryset = IssueCategory.objects.all()
    serializer_class = IssueCategorySerializer
    # permission_classes
