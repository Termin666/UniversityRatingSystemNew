# Generated by Django 4.2.1 on 2023-06-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educators', '0002_educator_personal_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='educator',
            name='scopus_id',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='scopus id'),
        ),
    ]
