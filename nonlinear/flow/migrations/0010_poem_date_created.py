# Generated by Django 2.0.5 on 2019-01-02 18:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0009_auto_20190102_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 18, 20, 21, 436605, tzinfo=utc)),
        ),
    ]