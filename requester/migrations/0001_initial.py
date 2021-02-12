# Generated by Django 3.1.5 on 2021-02-10 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestType', models.CharField(choices=[('SD', 'Submission Deadline'), ('T2', 'TYPE2'), ('T3', 'TYPE3'), ('OT', 'Other')], max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('accept_status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_requests', to=settings.AUTH_USER_MODEL)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
