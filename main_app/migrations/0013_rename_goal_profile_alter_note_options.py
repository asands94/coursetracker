# Generated by Django 5.0.4 on 2024-04-11 15:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_note'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goal',
            new_name='Profile',
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-date']},
        ),
    ]
