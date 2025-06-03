from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Department


class Command(BaseCommand):
    help = "Populate Department Data"

    def handle(self, *args, **kwargs):
        # get or create superuser
        self.stdout.write(self.style.NOTICE("Inside the populate Departement Command"))
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
        self.stdout.write(self.style.NOTICE("Start Creating Departments"))
        Department.objects.bulk_create(departments)
        self.stdout.write(self.style.NOTICE("Finish Creating Departments"))
        departments = Department.objects.all()
        print(f"Departments: {departments}")
        self.stdout.write(
            self.style.NOTICE('Successfully create departments "%s"' % departments)
        )
