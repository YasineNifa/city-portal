from api.models.abstract import SimpleModel


class IsuueCategory(SimpleModel):
    class Meta:
        verbose_name_plural = "Issue Categories"

    def __str__(self):
        return self.name
