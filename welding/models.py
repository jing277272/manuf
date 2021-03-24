from django.db import models
from datetime import datetime
# Create your models here.


class Parameters(models.Model):
    equipment = models.CharField(max_length=20, blank=True, null=True, verbose_name="设备")
    serial= models.CharField(max_length=3, blank=True, null=True, verbose_name="系列")
    squeeze= models.CharField(max_length=3, blank=True, null=True, verbose_name="预压")
    slope= models.CharField(max_length=3, blank=True, null=True, verbose_name="缓升")
    weld1= models.CharField(max_length=3 ,blank=True, null=True, verbose_name="通电1")
    cool1= models.CharField(max_length=3, blank=True, null=True, verbose_name="冷却1")
    weld2= models.CharField(max_length=3, blank=True, null=True, verbose_name="通电2")
    cool2= models.CharField(max_length=3, blank=True, null=True, verbose_name="冷却2")
    weld3= models.CharField(max_length=3, blank=True, null=True, verbose_name="通电3")
    dslope= models.CharField(max_length=3, blank=True, null=True, verbose_name="缓降")
    hold= models.CharField(max_length=3, blank=True, null=True, verbose_name="保持")
    heat1= models.CharField(max_length=3, blank=True, null=True, verbose_name="焊接1")
    heat2= models.CharField(max_length=3, blank=True, null=True, verbose_name="焊接2")
    heat3= models.CharField(max_length=3, blank=True, null=True, verbose_name="焊接3")
    gauge= models.CharField(max_length=3, blank=True, null=True, verbose_name="表压力")
    pressure= models.CharField(max_length=3, blank=True, null=True, verbose_name="加压力")

											
    

    class Meta:
        db_table = "w_parameters"


class Recipe(models.Model):

    item = models.CharField(max_length=20, blank=True, null=True, verbose_name="项目")
    part_no = models.CharField(max_length=20, blank=True, null=True, verbose_name="零件号")
    op = models.CharField(max_length=20, blank=True,null=True, verbose_name="工序")
    name = models.CharField(max_length=20, blank=True,null=True, verbose_name="名称")
    equipment = models.ForeignKey(to='Parameters',related_name = 'eq',on_delete=models.CASCADE, verbose_name="设备")
    m1 = models.CharField(max_length=20, blank=True, null=True, verbose_name="材料1")
    t1= models.CharField(max_length=20, blank=True, null=True, verbose_name="厚度1")
    m2= models.CharField(max_length=20, blank=True, null=True, verbose_name="材料2")
    t2= models.CharField(max_length=20, blank=True, null=True, verbose_name="厚度2")
    m3= models.CharField(max_length=20, blank=True, null=True, verbose_name="材料3")
    t3= models.CharField(max_length=20, blank=True, null=True, verbose_name="厚度3")

    diameter = models.CharField(max_length=20, blank=True, null=True, verbose_name="修磨直径（mm)")
    frequency = models.CharField(max_length=20, blank=True, null=True, verbose_name="修磨频次")
    modify = models.ForeignKey(blank=False, null=True, default='1', to='web.UserInfo', on_delete=models.CASCADE,verbose_name="修改者")
    modify_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

    def __str__(self):
        return "%s-%s" % (self.part_no, self.tool_no)

    class Meta:
        db_table = "w_recipe"
