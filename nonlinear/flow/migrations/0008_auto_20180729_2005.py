# Generated by Django 2.0.5 on 2018-07-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0007_auto_20180729_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
