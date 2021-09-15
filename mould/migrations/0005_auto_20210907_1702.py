# Generated by Django 3.1.6 on 2021-09-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mould', '0004_auto_20210705_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairparts',
            name='type',
            field=models.CharField(choices=[('2', 'TD镶块'), ('1', '冲头'), ('5', '其它'), ('4', '成型镶块'), ('3', '斜楔'), ('0', '凹模')], default='0', max_length=2, verbose_name='类型'),
        ),
    ]