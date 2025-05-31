from rest_framework import viewsets

from api.models import IssueComment
from api.serializers import IssueCommentSerializer


class IssueCommentViewSet(viewsets.ModelViewSet):
    queryset = IssueComment.objects.all()
    serializer_class = IssueCommentSerializer
    # permission_classes
