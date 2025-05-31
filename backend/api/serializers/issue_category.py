from rest_framework import serializers

from api.models import IssueCategory


class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = "__all__"
