# Generated by Django 3.2.5 on 2023-09-27 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_ownee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='ownee',
            new_name='owner',
        ),
    ]