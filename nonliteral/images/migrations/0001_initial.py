# Generated by Django 2.2.13 on 2020-11-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]