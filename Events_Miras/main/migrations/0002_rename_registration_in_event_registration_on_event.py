# Generated by Django 4.2.5 on 2024-05-30 15:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration_in_event',
            new_name='Registration_on_event',
        ),
    ]
