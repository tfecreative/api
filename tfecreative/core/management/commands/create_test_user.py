from django.core.management.base import BaseCommand
from tfecreative import settings
from tfecreative.core import models as core_models
from faker import Faker


fake = Faker()


class Command(BaseCommand):
    help = 'Create test user account with profile.'

    def handle(self, *args, **options):
        user = self.create_user()
        self.create_profile(user)

    def create_profile(self, user):
        profile, created = core_models.UserProfile.objects.get_or_create(
            user=user
        )
        self.stdout.write(self.style.SUCCESS(f'[*] Created profile for user'))
        return profile

    def create_user(self):
        try:
            test_user = core_models.TfeUser.objects.get(
                email=settings.TEST_USER_EMAIL
            )
        except core_models.TfeUser.DoesNotExist:
            test_user, created = core_models.TfeUser.objects.get_or_create(
                email=settings.TEST_USER_EMAIL,
                username=settings.TEST_USER_USERNAME,
                first_name=settings.TEST_USER_FIRST_NAME,
                last_name=settings.TEST_USER_LAST_NAME,
            )
            test_user.set_password(settings.TEST_USER_PASSWORD)
            test_user.save()
        self.stdout.write(self.style.SUCCESS(f'[*] Created test user'))
        return test_user
