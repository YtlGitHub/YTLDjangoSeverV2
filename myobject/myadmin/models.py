from django.db import models
from datetime import datetime
# Create your models here.


class PrototypeInfo(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_info"  # 表名
        verbose_name = '杨天龙样机信息'
        verbose_name_plural = '杨天龙样机管理'


class PrototypeHzx(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_hzx"  # 表名
        verbose_name = '何振兴样机信息'
        verbose_name_plural = '何振兴样机管理'


class PrototypeJxl(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_jxl"  # 表名
        verbose_name = '蒋小丽样机信息'
        verbose_name_plural = '蒋小丽样机管理'


class Prototypeztw(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_ztw"  # 表名
        verbose_name = '郑廷威样机信息'
        verbose_name_plural = '郑廷威样机管理'


class Prototypewjy(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_wjy"  # 表名
        verbose_name = '王杰玉样机信息'
        verbose_name_plural = '王杰玉样机管理'


class Prototypelzx(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_lzx"  # 表名
        verbose_name = '刘志霞样机信息'
        verbose_name_plural = '刘志霞样机管理'


class Prototypepyc(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_pyc"  # 表名
        verbose_name = '彭雨超样机信息'
        verbose_name_plural = '彭雨超样机管理'


class Prototypexth(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_xth"  # 表名
        verbose_name = '许天华样机信息'
        verbose_name_plural = '许天华样机管理'


class Prototypehwp(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_hwp"  # 表名
        verbose_name = '黄伟鹏样机信息'
        verbose_name_plural = '黄伟鹏样机管理'


class Prototypelkx(models.Model):
    '''自定义PrototypeInfo表对应的Model类'''
    # 定义属性：主键默认自增id可不写
    id = models.AutoField(primary_key=True)
    id_name = models.IntegerField('项目代号')
    de = models.CharField('销售', max_length=25)
    brand = models.CharField('品牌', max_length=25)
    pv = models.IntegerField('安卓版本', max_length=2)
    os = models.CharField('OS', max_length=10)
    m_name = models.CharField('机型名', max_length=25)
    IMEI = models.CharField(max_length=25)
    name = models.CharField('样机管理员', max_length=10)
    user_name = models.CharField('样机借用人', max_length=10)
    borrow_time = models.DateTimeField('借用时间', default=datetime.now())
    still_time = models.DateTimeField('归还时间', blank=True)
    备注 = models.CharField('备注', max_length=255, blank=True)

    def __str__(self):
        return f'{self.id,self.id_name,self.de,self.brand,self.pv,self.os,self.m_name,self.IMEI,self.name,self.user_name,self.borrow_time,self.still_time,self.备注}'

    class Meta():
        db_table = "prototype_lkx"  # 表名
        verbose_name = '刘康欣样机信息'
        verbose_name_plural = '刘康欣样机管理'


class Material(models.Model):  # 物料记录
    name = models.CharField('姓名', max_length=20)
    material = models.CharField('物料', max_length=20)
    gave_time = models.DateTimeField('借给时间', default=datetime.now())
    sum = models.IntegerField('剩余数量')

    def __str__(self):
        return f'{self.name,self.material,self.gave_time,self.sum}'

    class Meta:
        db_table = 'material'
        verbose_name_plural = '物料管理'
        verbose_name = '物料信息'


class Discipline(models.Model):  # 违规记录
    name = models.CharField('姓名', max_length=20)
    job_number = models.CharField('工号', max_length=20)
    supplier = models.CharField('部门', max_length=20)
    violation = models.CharField('记录', max_length=255)
    time = models.DateTimeField('时间', max_length=255)
    actual = models.CharField('实际', max_length=50)
    fine = models.CharField('罚款', max_length=10)
    money = models.IntegerField('金额')

    # def __str__(self):
    #     return f'{self.name,self.material,self.gave_time,self.sum}'

    class Meta:
        db_table = 'discipline'
        verbose_name_plural = '违规记录管理'
        verbose_name = '违规记录'