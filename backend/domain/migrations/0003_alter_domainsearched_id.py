# Generated by Django 3.2.6 on 2021-08-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0002_auto_20210823_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainsearched',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]