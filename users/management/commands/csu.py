from django.core.management import BaseCommand

from users.models import User

"""Команда для создания администратора приложения"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com", is_superuser=True)
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
