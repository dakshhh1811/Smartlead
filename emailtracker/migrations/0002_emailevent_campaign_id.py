# Generated by Django 5.2.1 on 2025-05-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailtracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailevent',
            name='campaign_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
