from django.core.management.base import BaseCommand
from tfecreative import settings
from tfecreative.core.models import TfeUser, UserProfile


class Command(BaseCommand):
    help = 'Create admin (superuser).'

    def handle(self, *args, **options):
        self.create_admin()

    def create_admin(self):
        """ Creates the Admin SuperUser for API and Admin Panel access """
        self.stdout.write('[*] Checking for existing Admin user...')
        try:
            TfeUser.objects.get(username=settings.ADMIN_USERNAME)
            self.stdout.write('[*] Found an existing admin...')
            self.stdout.write('[*] Returning!')
            return
        except TfeUser.DoesNotExist:
            self.stdout.write('[*] Existing admin not found!')

        # create user
        admin = TfeUser.objects.create_superuser(
            email=settings.ADMIN_EMAIL,
            username=settings.ADMIN_USERNAME,
            password=settings.ADMIN_PASSWORD,
        )
        self.stdout.write(self.style.SUCCESS('[*] Created admin'))

        # create profile
        profile, created = UserProfile.objects.get_or_create(user=admin)
        self.stdout.write(self.style.SUCCESS(
            '[*] Created profile for admin'
        ))
