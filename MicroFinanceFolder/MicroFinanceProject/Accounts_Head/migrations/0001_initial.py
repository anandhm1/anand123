# Generated by Django 4.0.3 on 2022-03-15 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Operational_Head', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanction_amt', models.FloatField()),
                ('rate_of_interest', models.FloatField()),
                ('loan_tenure', models.IntegerField()),
                ('total_amt', models.FloatField()),
                ('is_customer_responsed', models.BooleanField(default=False, verbose_name='proceed')),
                ('is_emi_details_filled', models.BooleanField(default=False, verbose_name='Yes')),
                ('loan_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Operational_Head.loansaction')),
            ],
        ),
        migrations.CreateModel(
            name='Emi_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothly_emi_amt', models.FloatField()),
                ('interest', models.FloatField()),
                ('gst', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('due_date', models.DateField()),
                ('last_payment_status', models.CharField(max_length=200)),
                ('customer_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('sanction_amt', models.FloatField()),
                ('account_head', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts_Head.account_head')),
            ],
        ),
    ]
