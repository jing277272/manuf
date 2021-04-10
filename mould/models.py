from django.conf import settings
from django.db import models


# Create your models here.

class Item(models.Model):
    list_display = ("part_no",)
    part_no = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.part_no

    class Meta:
        db_table = "item"


class Mould(models.Model):
    LINE_CHOICES = (
        ('0', 'BLK'),
        ('1', 'PRG'),
        ('2', '大线四线'),
        ('3', '大线手工线'),
        ('4', '中线'),
        ('5', '小线'),
        ('6', '专线2线'),
        ('7', '专线3线'),
        ('8', '专线4线'),
        ('9', '自动化1线'),
        ('A', '自动化2线'),
        ('B', '自动化3线'),
    )
    STATUS_CHOICES = (
        ('0', '闲置'),
        ('1', '在用'),
    )
    item = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="项目")
    assy_no = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="总成号")
    part_no = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="零件号")
    tool_no = models.CharField(
        max_length=20, blank=True, unique=True, null=False, verbose_name="工装编号", db_index=True)
    op = models.CharField(max_length=20, blank=True,
                          null=True, verbose_name="工序")
    name = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name="名称")
    equipment = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="设备")
    line = models.CharField(
        max_length=1, choices=LINE_CHOICES, blank=True, null=True, verbose_name="线别")
    live = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name="设计寿命")
    marker = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="制造商")
    order_date = models.DateTimeField(
        null=True, blank=True, verbose_name="量产时间")
    zc_id = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name="资产编号")
    qr_id = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name="二维码")
    user_dp = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="使用部门")
    manage_dp = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="管理部门")
    site = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name="存放地点")
    status = models.BooleanField(default=True, verbose_name="使用状态")
    owner = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name="资产所属")
    remark = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="备注")
    location = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="定置编码")
    img_upper = models.ImageField(
        upload_to="record/", blank=True, verbose_name="上模图片")
    img_downer = models.ImageField(
        upload_to="record/", blank=True, verbose_name="下模图片")
    img_assy = models.ImageField(
        upload_to="record/", blank=True, verbose_name="合模图片")
    img_op = models.ImageField(
        upload_to="record/", blank=True, verbose_name="工序图片")
    length = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="长")
    width = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name="宽")
    height = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="高")
    weight_upper = models.IntegerField(
        default=0, blank=False, verbose_name="上模重量")
    weight_assy = models.IntegerField(
        default=0, blank=False, verbose_name="模具重量")
    repair_count = models.IntegerField(
        default=0, blank=True, verbose_name="维修次数")
    repair_time = models.TimeField(blank=True, null=True, verbose_name="维修时长")
    modify = models.ForeignKey(blank=False, null=True, default='1', to='web.UserInfo', on_delete=models.CASCADE,
                               verbose_name="修改者")
    modify_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

    def __str__(self):
        return "%s-%s" % (self.part_no, self.tool_no)

    class Meta:
        db_table = "m_mould"


class RepairParts(models.Model):
    type_choices = {
        ('0', '凹模'),
        ('1', '冲头'),
        ('2', 'TD镶块'),
        ('3', '斜楔'),
        ('4', '成型镶块'),
        ('5', '其它'),
        }
    tool = models.ForeignKey(
        'Mould', related_name='repairpart', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2, choices=type_choices, default='0', verbose_name="类型")
    imgs = models.ImageField(upload_to='repair/', blank=True, null=True, verbose_name="照片")
    modify_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    local = models.CharField(max_length=20, 
                             null=False, verbose_name="货位号")
    quantity = models.PositiveIntegerField(
        null=True, default=1, verbose_name="在库数量")
    modify = models.ForeignKey(blank=False, null=True, default='1', to='web.UserInfo', on_delete=models.CASCADE,
                               verbose_name="修改者")

    class Meta:
        db_table = "m_RepairParts"


class FaultPost(models.Model):
    POST_CHOICES = (
        ('0', 'BLK'),
        ('1', 'PRG'),
        ('2', '大线四线'),
        ('3', '大线手工线'),
        ('4', '中线'),
        ('5', '小线'),
        ('6', '专线2线'),
        ('7', '专线3线'),
        ('8', '专线4线'),
        ('9', '自动化1线'),
        ('A', '自动化2线'),
        ('B', '自动化3线'),
    )
    RESULT_CHOICES = (
        ('0', '在线维修完毕'),
        ('1', '拆模维修'),
        ('2', '放行生产，下线维修'),
    )
    tool = models.ForeignKey(
        'Mould', to_field='tool_no', on_delete=models.CASCADE)
    content = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="故障内容")
    fault_date = models.DateField(verbose_name="故障日期")
    start_time = models.TimeField(verbose_name="故障开始")
    end_time = models.TimeField(verbose_name="故障结束")
    reasons = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="故障分析")
    solve = models.CharField(max_length=20, blank=False,
                             null=False, verbose_name="处理对策")
    position = models.CharField(
        max_length=1, choices=POST_CHOICES, blank=True, null=True, verbose_name="故障部位")
    imgs = models.ImageField(upload_to='fault/', blank=True, null=True)
    result = models.CharField(
        max_length=1, choices=RESULT_CHOICES, default='0', verbose_name="维修结果")
    ab_product = models.IntegerField(
        default=0, blank=False, verbose_name="调模件")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True)
    servicemen = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE,
                                   verbose_name="维修人员")

    class Meta:
        db_table = "m_FaultPost"
