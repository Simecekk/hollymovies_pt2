from django.contrib.auth.models import Permission
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType

from movie import general_permissions


class Command(BaseCommand):
    help = 'Create Custom permissions'

    def handle(self, *args, **options):
        print('Creating general permissions started')
        content_type, _ = ContentType.objects.get_or_create(
            app_label=general_permissions.APP_LABEL,
            model=general_permissions.MODEL,
        )
        for codename, name in general_permissions.GENERAL_PERMISSIONS.items():
            _, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type,
            )
            if created:
                print(f'Created permission: {codename}')
        print('Creating general permission finished')
