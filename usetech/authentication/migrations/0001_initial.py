# Generated by Django 4.2.5 on 2023-09-30 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=256)),
                ('secret', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='authentication.client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_service', to='authentication.service')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='allowed_services',
            field=models.ManyToManyField(through='authentication.UserService', to='authentication.service'),
        ),
    ]