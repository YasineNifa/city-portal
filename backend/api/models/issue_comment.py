from django.db import models
from django.contrib.auth.models import User

from api.models.abstract import SimpleModel


class IssueComment(SimpleModel):
    issue = models.ForeignKey(
        "api.Issue",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="issue_comments",
    )

    def __str__(self):
        return f"Comment by {self.user.username} on {self.issue.name}"
