# Generated by Django 3.1.6 on 2021-04-19 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Mould',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=20, null=True, verbose_name='项目')),
                ('assy_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='总成号')),
                ('part_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='零件号')),
                ('tool_no', models.CharField(blank=True, db_index=True, max_length=20, unique=True, verbose_name='工装编号')),
                ('op', models.CharField(blank=True, max_length=20, null=True, verbose_name='工序')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='名称')),
                ('equipment', models.CharField(blank=True, max_length=20, null=True, verbose_name='设备')),
                ('line', models.CharField(blank=True, choices=[('0', 'BLK'), ('1', 'PRG'), ('2', '大线四线'), ('3', '大线手工线'), ('4', '中线'), ('5', '小线'), ('6', '专线2线'), ('7', '专线3线'), ('8', '专线4线'), ('9', '自动化1线'), ('A', '自动化2线'), ('B', '自动化3线')], max_length=1, null=True, verbose_name='线别')),
                ('live', models.CharField(blank=True, max_length=20, null=True, verbose_name='设计寿命')),
                ('marker', models.CharField(blank=True, max_length=20, null=True, verbose_name='制造商')),
                ('order_date', models.DateTimeField(blank=True, null=True, verbose_name='量产时间')),
                ('zc_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='资产编号')),
                ('qr_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='二维码')),
                ('user_dp', models.CharField(blank=True, max_length=20, null=True, verbose_name='使用部门')),
                ('manage_dp', models.CharField(blank=True, max_length=20, null=True, verbose_name='管理部门')),
                ('site', models.CharField(blank=True, max_length=20, null=True, verbose_name='存放地点')),
                ('status', models.BooleanField(default=True, verbose_name='使用状态')),
                ('owner', models.CharField(blank=True, max_length=20, null=True, verbose_name='资产所属')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('location', models.CharField(blank=True, max_length=20, null=True, verbose_name='定置编码')),
                ('img_upper', models.ImageField(blank=True, upload_to='record/', verbose_name='上模图片')),
                ('img_downer', models.ImageField(blank=True, upload_to='record/', verbose_name='下模图片')),
                ('img_assy', models.ImageField(blank=True, upload_to='record/', verbose_name='合模图片')),
                ('img_op', models.ImageField(blank=True, upload_to='record/', verbose_name='工序图片')),
                ('length', models.CharField(blank=True, max_length=20, null=True, verbose_name='长')),
                ('width', models.CharField(blank=True, max_length=20, null=True, verbose_name='宽')),
                ('height', models.CharField(blank=True, max_length=20, null=True, verbose_name='高')),
                ('weight_upper', models.IntegerField(default=0, verbose_name='上模重量')),
                ('weight_assy', models.IntegerField(default=0, verbose_name='模具重量')),
                ('repair_count', models.IntegerField(blank=True, default=0, verbose_name='维修次数')),
                ('repair_time', models.TimeField(blank=True, null=True, verbose_name='维修时长')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('modify', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='web.userinfo', verbose_name='修改者')),
            ],
            options={
                'db_table': 'm_mould',
            },
        ),
        migrations.CreateModel(
            name='RepairParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('2', 'TD镶块'), ('3', '斜楔'), ('4', '成型镶块'), ('0', '凹模'), ('5', '其它'), ('1', '冲头')], default='0', max_length=2, verbose_name='类型')),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='repair/', verbose_name='照片')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('local', models.CharField(max_length=20, verbose_name='货位号')),
                ('quantity', models.PositiveIntegerField(default=1, null=True, verbose_name='在库数量')),
                ('modify', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='web.userinfo', verbose_name='修改者')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairpart', to='mould.mould')),
            ],
            options={
                'db_table': 'm_RepairParts',
            },
        ),
        migrations.CreateModel(
            name='FaultPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='故障内容')),
                ('fault_date', models.DateField(verbose_name='故障日期')),
                ('start_time', models.TimeField(verbose_name='故障开始')),
                ('end_time', models.TimeField(verbose_name='故障结束')),
                ('reasons', models.CharField(max_length=200, verbose_name='故障分析')),
                ('solve', models.CharField(max_length=20, verbose_name='处理对策')),
                ('position', models.CharField(blank=True, choices=[('0', 'BLK'), ('1', 'PRG'), ('2', '大线四线'), ('3', '大线手工线'), ('4', '中线'), ('5', '小线'), ('6', '专线2线'), ('7', '专线3线'), ('8', '专线4线'), ('9', '自动化1线'), ('A', '自动化2线'), ('B', '自动化3线')], max_length=1, null=True, verbose_name='故障部位')),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='fault/')),
                ('result', models.CharField(choices=[('0', '在线维修完毕'), ('1', '拆模维修'), ('2', '放行生产，下线维修')], default='0', max_length=1, verbose_name='维修结果')),
                ('ab_product', models.IntegerField(default=0, verbose_name='调模件')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('servicemen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='维修人员')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mould.mould', to_field='tool_no')),
            ],
            options={
                'db_table': 'm_FaultPost',
            },
        ),
    ]
