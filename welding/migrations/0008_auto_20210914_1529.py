# Generated by Django 3.1.6 on 2021-09-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welding', '0007_parameters_eq_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='GunSel',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='钳选择'),
        ),
        migrations.AddField(
            model_name='parameters',
            name='TurnR',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='匝数比'),
        ),
    ]