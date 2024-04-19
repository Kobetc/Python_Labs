# Generated by Django 5.0.4 on 2024-04-19 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('companyName', models.CharField(max_length=255, verbose_name='Имя компании')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('successCount', models.IntegerField(default=0, verbose_name='Число успешных устройств')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('experience', models.IntegerField(default=0, verbose_name='Стаж работы')),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employer')),
                ('recruiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.recruiter')),
            ],
        ),
    ]
