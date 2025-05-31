from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Department


class Command(BaseCommand):
    help = "POpulate Department Data"

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username="admin").first()
        if not user:
            user = User.objects.create_superuser(username="admin", password="test")

        # create departments - name
        departments = [
            Department(
                name="Electricité",
            ),
            Department(
                name="Gaz",
            ),
            Department(
                name="Mobilité",
            ),
            Department(
                name="Multimédia",
            ),
            Department(
                name="Rural",
            ),
        ]

        # create Departments & re-fetch from DB
        Department.objects.bulk_create(departments)
        departments = Department.objects.all()
