# Generated by Django 5.1.6 on 2025-02-19 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('api_endpoint', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_input', models.TextField()),
                ('response', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('model_used', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatapp.modelprovider')),
            ],
        ),
        migrations.CreateModel(
            name='RegexRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=255)),
                ('model_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.modelprovider')),
            ],
        ),
    ]
