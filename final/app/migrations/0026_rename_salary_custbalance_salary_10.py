# Generated by Django 4.2.1 on 2023-10-02 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_custbalance_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custbalance',
            old_name='salary',
            new_name='salary_10',
        ),
    ]