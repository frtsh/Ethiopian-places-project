from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from frtuna.models import destinations
import json
import os

class Command(BaseCommand):
    help = 'Create a superuser and add destinations from destinations.json.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'frtuna'
        password = 'admin'
        email = 'frtuna@gmail.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))

        # Load destinations from destinations.json
        json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '..', '..', 'destinations.json')
        json_path = os.path.abspath(json_path)
        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f'destinations.json not found at {json_path}'))
            return
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        added = 0
        for entry in data:
            fields = entry['fields']
            pk = entry['pk']
            if not destinations.objects.filter(pk=pk).exists():
                destinations.objects.create(
                    id=pk,
                    name=fields['name'],
                    img=fields['img'],
                    desc=fields['desc'],
                    price=fields['price'],
                    offer=fields['offer']
                )
                added += 1
        self.stdout.write(self.style.SUCCESS(f'Added {added} new destinations.')) 