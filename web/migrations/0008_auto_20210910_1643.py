# Generated by Django 3.1.6 on 2021-09-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20210910_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='mode',
            field=models.SmallIntegerField(choices=[(2, '隐私模式'), (1, '公开模式')], default=1, verbose_name='模式'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='priority',
            field=models.CharField(choices=[('warning', '中'), ('danger', '高'), ('success', '低')], default='danger', max_length=12, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.SmallIntegerField(choices=[(7, '重新打开'), (2, '处理中'), (5, '待反馈'), (6, '已关闭'), (4, '已忽略'), (1, '新建'), (3, '已解决')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='pricepolicy',
            name='category',
            field=models.SmallIntegerField(choices=[(3, '其他'), (2, '收费版'), (1, '免费版')], default=2, verbose_name='收费类型'),
        ),
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.SmallIntegerField(choices=[(6, '#7461c2'), (3, '#ebc656'), (2, '#f28033'), (5, '#20bFA4'), (7, '#20bfa3'), (4, '#a2d148'), (1, '#56b8eb')], default=1, verbose_name='颜色'),
        ),
    ]
