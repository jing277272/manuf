# Generated by Django 3.1.6 on 2021-09-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mould', '0011_auto_20210914_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairparts',
            name='type',
            field=models.CharField(choices=[('0', '凹模'), ('1', '冲头'), ('5', '其它'), ('2', 'TD镶块'), ('4', '成型镶块'), ('3', '斜楔')], default='0', max_length=2, verbose_name='类型'),
        ),
    ]
