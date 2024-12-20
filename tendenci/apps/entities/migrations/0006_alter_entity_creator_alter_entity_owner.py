# Generated by Django 4.2.11 on 2024-08-18 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0005_entity_show_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='creator',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entity',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
