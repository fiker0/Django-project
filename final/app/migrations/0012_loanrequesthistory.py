# Generated by Django 4.2.1 on 2023-06-03 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_loanrequest_reject_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanRequestHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('loan_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loanrequest')),
            ],
        ),
    ]
