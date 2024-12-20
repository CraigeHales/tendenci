# Generated by Django 4.2.11 on 2024-08-18 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0006_alter_entity_creator_alter_entity_owner'),
        ('navs', '0003_auto_20201028_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav',
            name='creator',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nav',
            name='entity',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entity', to='entities.entity'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
