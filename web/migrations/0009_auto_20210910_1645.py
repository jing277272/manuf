# Generated by Django 3.1.6 on 2021-09-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20210910_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='mode',
            field=models.SmallIntegerField(choices=[(1, '公开模式'), (2, '隐私模式')], default=1, verbose_name='模式'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='priority',
            field=models.CharField(choices=[('danger', '高'), ('success', '低'), ('warning', '中')], default='danger', max_length=12, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '新建'), (3, '已解决'), (7, '重新打开'), (6, '已关闭'), (5, '待反馈'), (4, '已忽略'), (2, '处理中')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.SmallIntegerField(choices=[(6, '#7461c2'), (5, '#20bFA4'), (2, '#f28033'), (3, '#ebc656'), (4, '#a2d148'), (1, '#56b8eb'), (7, '#20bfa3')], default=1, verbose_name='颜色'),
        ),
    ]