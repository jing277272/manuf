# Generated by Django 3.1.6 on 2021-09-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welding', '0005_parameters_etype'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='line',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='线别'),
        ),
    ]
