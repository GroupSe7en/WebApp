# Generated by Django 3.1.5 on 2021-02-07 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_studentprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]
