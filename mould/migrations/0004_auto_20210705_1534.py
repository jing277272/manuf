# Generated by Django 3.1.6 on 2021-07-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mould', '0003_auto_20210705_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairparts',
            name='type',
            field=models.CharField(choices=[('1', '冲头'), ('5', '其它'), ('4', '成型镶块'), ('0', '凹模'), ('3', '斜楔'), ('2', 'TD镶块')], default='0', max_length=2, verbose_name='类型'),
        ),
    ]