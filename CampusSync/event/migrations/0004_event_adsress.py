# Generated by Django 5.0.3 on 2024-04-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='adsress',
            field=models.CharField(default='hetherere', max_length=200),
            preserve_default=False,
        ),
    ]