from api.models.abstract import NamedModel, DatedModel


class Department(DatedModel, NamedModel):
    def __str__(self):
        return self.name
