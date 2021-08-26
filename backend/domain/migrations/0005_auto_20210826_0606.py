# Generated by Django 3.2.6 on 2021-08-26 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0004_auto_20210824_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainsearched',
            name='name',
        ),
        migrations.RemoveField(
            model_name='domainsearched',
            name='searchers',
        ),
        migrations.AddField(
            model_name='domainsearched',
            name='searches',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='domainsearched',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
