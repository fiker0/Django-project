# Generated by Django 4.2.1 on 2023-07-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_customerprofile_address_customerprofile_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='count',
        ),
    ]
