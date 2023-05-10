# Generated by Django 4.1.7 on 2023-04-26 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='department type name')),
            ],
            options={
                'verbose_name': 'department type',
                'verbose_name_plural': 'department types',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='department name')),
                ('department_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departments.departmenttype', verbose_name='department type')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faculties.faculty', verbose_name='department faculty')),
                ('head', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='department head profile')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
            },
        ),
    ]
