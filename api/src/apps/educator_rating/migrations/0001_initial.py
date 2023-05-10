# Generated by Django 4.1.7 on 2023-04-26 17:25

import apps.educator_rating.fields
import apps.rating.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0001_initial'),
        ('educators', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducatorReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='report UUID')),
                ('year', apps.educator_rating.fields.ValidRatingYearField(validators=[django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2023)], verbose_name='report year')),
                ('approved', models.BooleanField(default=False, verbose_name='report approved status')),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educators.educator', verbose_name='educator')),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
                'unique_together': {('educator', 'year')},
            },
        ),
        migrations.CreateModel(
            name='EducatorRatingPartition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rating.ratingpartition', verbose_name='rating partition')),
            ],
            options={
                'verbose_name': 'educator rating partition',
                'verbose_name_plural': 'educator rating partitions',
            },
        ),
        migrations.CreateModel(
            name='EducatorReportController',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educator_report_controllers', to='departments.department', verbose_name='responsible department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='controller profile')),
            ],
            options={
                'verbose_name': 'controller',
                'verbose_name_plural': 'controllers',
                'unique_together': {('user', 'department')},
            },
        ),
        migrations.CreateModel(
            name='EducatorIndicatorValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField(validators=[apps.rating.validators.validate_indicator_value], verbose_name='indicator value')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.indicator', verbose_name='indicator')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educator_rating.educatorreport', verbose_name='educator report')),
            ],
            options={
                'verbose_name': 'indicator value',
                'verbose_name_plural': 'indicator values',
                'unique_together': {('indicator', 'report')},
            },
        ),
    ]
