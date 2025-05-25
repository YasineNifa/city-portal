from django.db import models


class NamedModel(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class DatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class SimpleModel(NamedModel, DatedModel):
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
