# Generated by Django 3.1.5 on 2021-03-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requester', '0009_auto_20210314_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrequest',
            name='requestType',
            field=models.CharField(choices=[('SD', 'Extending Submission Deadline'), ('LR', 'Leave Request'), ('RL', 'Rescheduling of a Lecture'), ('MR', 'Miscellaneous Request')], max_length=2, verbose_name='Type of the request'),
        ),
    ]
