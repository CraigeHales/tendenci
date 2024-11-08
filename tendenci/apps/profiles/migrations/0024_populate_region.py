# Generated by Django 4.2.13 on 2024-07-17 15:15

from django.db import migrations


def populate_region(apps, schema_editor):
    from tendenci.apps.profiles.models import Profile
    for profile in Profile.objects.all():
        if profile.membership and profile.membership.region:
            profile.region = profile.membership.region
            profile.save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_profile_region'),
    ]

    operations = [
        migrations.RunPython(populate_region),
    ]