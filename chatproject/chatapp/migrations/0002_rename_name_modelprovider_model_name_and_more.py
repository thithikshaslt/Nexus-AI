# Generated by Django 5.1.6 on 2025-02-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelprovider',
            old_name='name',
            new_name='model_name',
        ),
        migrations.RemoveField(
            model_name='modelprovider',
            name='api_endpoint',
        ),
        migrations.AddField(
            model_name='modelprovider',
            name='provider_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
