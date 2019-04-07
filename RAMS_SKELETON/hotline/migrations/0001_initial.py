# Generated by Django 2.1.7 on 2019-04-07 00:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ser_req',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('attended_to', models.BooleanField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
                ('verbal_permission', models.BooleanField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('key_provided', models.BooleanField(blank=True, null=True)),
                ('forced_entry', models.BooleanField(blank=True, null=True)),
                ('outcome', models.TextField(blank=True, null=True)),
                ('owner_notification_notes', models.TextField(blank=True, null=True)),
                ('recovery_time', models.DateTimeField(blank=True, null=True)),
                ('owner_notification_tstamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': [],
            },
        ),
    ]
