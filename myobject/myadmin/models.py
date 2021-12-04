from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    '''自定义User类'''
    username = models.CharField(max_length=50)  # 员工账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=1)  # 状态：1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        print('create_at', self.create_at, 'update_at', self.update_at)
        return {'id': self.id, 'username': self.username, 'nickname': self.nickname, 'password_hash': self.password_hash, 'password_salt': self.password_salt, 'status': self.status, 'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"), 'update_at': self.update_at.strftime("%Y-%m-%d %H:%M:%S")}

    class Meta:
        db_table = "user"  # 指定表面


class Family(models.Model):
    '''自定义family类'''
    name = models.CharField('姓名', max_length=25)
    age = models.IntegerField('年龄')
    sex = models.CharField('性别', max_length=10)
    address = models.CharField('现住地址', max_length=50)
    phone = models.IntegerField('电话号码', max_length=16)
    birthday = models.DateTimeField('出生日期', blank=True)
    addTime = models.DateTimeField('添加时间', blank=True)

    def __str__(self):
        pass

    class Meta():
        db_table = "family"  # 表名
        verbose_name = '杨天龙家庭信息管理'
        verbose_name_plural = '杨天龙家庭信息'


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
        verbose_name = '样机'
        verbose_name_plural = '兼容已录入样机信息管理'


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
    actual = models.CharField('实际', max_length=50, blank=True)
    fine = models.CharField('罚款', max_length=10, blank=True)
    money = models.IntegerField('金额', blank=True)

    # def __str__(self):
    #     return f'{self.name,self.material,self.gave_time,self.sum}'

    class Meta:
        db_table = 'discipline'
        verbose_name_plural = '违规记录管理'
        verbose_name = '违规记录'