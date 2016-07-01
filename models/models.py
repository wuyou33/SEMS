# coding=utf-8
from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    card_number = models.IntegerField(null=False)
    student_number = models.IntegerField(null=False)
    username = models.CharField(null=False, max_length=45)
    openid = models.CharField(null=False, max_length=45, blank=True)
    password = models.CharField(null=False, max_length=16)
    phone_number = models.CharField(null=False, max_length=45, blank=True)
    usage = models.IntegerField(default=1)   #用以标记用户的可用度
    default_money = models.FloatField(default=0.00) #用户上次拖欠金额

    def __unicode__(self):
        return u'用户名：%s,学号：%d,卡号：%d' % (self.username, self.student_number,self.card_number)

    class Meta:
        verbose_name_plural = "用户"


class Manager(models.Model):
    name = models.CharField(null=False, max_length=45)
    password = models.CharField(null=False, max_length=16)
    POWER_CHOICE = (('0', 'GENERAL'), ('1', 'ASSOCIATE'))
    power = models.CharField(max_length=1, choices=POWER_CHOICE)

    def __unicode__(self):
        return u'管理员：%s,权限：%s' % (self.name, self.power)

    class Meta:
        verbose_name_plural = "管理员"



class AmmeterGroup(models.Model):
    name = models.CharField(null=False,max_length=50)
    longitude = models.FloatField()  # 经度
    latitude = models.FloatField()  # 纬度

    def __unicode__(self):
        return u'id:%s 组名：%s 经度：%f,纬度：%f,' % (self.id,self.name, self.longitude, self.latitude)

    class Meta:
        verbose_name_plural = "充电站组"


class Ammeter(models.Model):
    name = models.CharField(null=False, max_length=45)
    STATUS_CHOICE = (('0', 'ON'), ('1', 'OFF'), ('2', 'Low'), ('3', 'ABNORMAL'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    group = models.ForeignKey(AmmeterGroup)

    def __unicode__(self):
        return u'id : %s 电表名：%s,状态：%s' % (self.id, self.name, self.status)

    class Meta:
        verbose_name_plural = "充电站"


class Charge(models.Model):
    user = models.ForeignKey(User)
    ammeter = models.ForeignKey(Ammeter)
    STATUS_CHOICE = (('0', 'CHARGING'), ('1', 'DONE'), ('2', 'ABNORMAL'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    start_time = models.DateTimeField(null=False, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)
    overtime = models.IntegerField(default=0)
    message = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = "充电记录"


    def __unicode__(self):
        return u'用户名：%s,电表id：%s,状态：%s,开始时间：%s,结束时间：%s' % (
            self.user.username, self.ammeter.id, self.status, self.start_time, self.end_time)


class Account(models.Model):
    charge = models.ForeignKey(Charge)
    money = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=0.00)
    message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return u'充电记录id：%d,金额：%f' % (self.charge_id, self.money)

    class Meta:
        verbose_name_plural = "消费记录"
