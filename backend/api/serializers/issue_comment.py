from rest_framework import serializers

from api.models import IssueComment


class IssueCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueComment
        fields = "__all__"
