from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User

from api.models.abstract import SimpleModel
from api.models.department import Department
from api.models.issue_category import IssueCategory


class Issue(SimpleModel):
    STATUS_SUBMITTED = 0
    STATUS_ASSIGNED = 1
    STATUS_RESOLVED = 2
    STATUS_CHOICES = (
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_ASSIGNED, "Assigned"),
        (STATUS_RESOLVED, "Resolved"),
    )
    PRIORITY_LOW = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_HIGH = 2
    PRIORITY_CHOICES = (
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
    )

    category = models.ForeignKey(
        IssueCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="issues",
    )
    location = gis_models.PointField(
        srid=4326,  # SRID 4326 for lat/lon
        null=True,
        blank=True,
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_SUBMITTED,
    )
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES,
        default=PRIORITY_LOW,
        null=True,
        blank=True,
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reported_issues",
    )
    assigned_to_department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="assigned_issues",
    )
    assigned_to_staff_member = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="handling_issues",
        limit_choices_to={
            "groups__name__in": ["Staff", "Admin"]
        },  # Ensure only staff/admin can be assigned
    )
    resolution_details = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
