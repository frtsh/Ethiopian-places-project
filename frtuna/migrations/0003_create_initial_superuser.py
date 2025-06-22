from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    username = "frtuna"  # CHANGE THIS after confirmation
    email = "frtuna@gmail.com"  # CHANGE THIS after confirmation
    password = "frtunaadmin"  # CHANGE THIS after confirmation
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

class Migration(migrations.Migration):

    dependencies = [
        ('frtuna', '0002_destinations_price'),  # Adjust if your latest migration is different
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ] 