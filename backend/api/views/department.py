from rest_framework import viewsets

from api.models import Department
from api.serializers import DepartmentSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes
