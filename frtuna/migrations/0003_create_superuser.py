from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='ChangeThisPassword123!'
    )

class Migration(migrations.Migration):
    dependencies = [
        ('frtuna', '0002_destinations_price'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ] 