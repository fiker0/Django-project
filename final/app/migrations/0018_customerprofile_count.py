# Generated by Django 4.2.1 on 2023-06-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_balance_adminprofile_balance1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]