# Generated by Django 4.0.3 on 2022-03-15 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Operational_Head', '0002_alter_loansaction_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loansaction',
            name='customer',
        ),
        migrations.AddField(
            model_name='loansaction',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='b', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
