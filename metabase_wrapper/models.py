import datetime
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_default_sku():
    return Sku.objects.get_or_create(name='ПРОВЕРИТЬ', code=0)[0]

def get_default_channel1():
    return Channel1.objects.get_or_create(name='ПРОВЕРИТЬ')[0]

def get_default_channel2():
    return Channel2.objects.get_or_create(name='ПРОВЕРИТЬ')[0]

def get_default_format1():
    return Format1.objects.get_or_create(name='ПРОВЕРИТЬ')[0]

def get_default_format2():
    return Format2.objects.get_or_create(name='ПРОВЕРИТЬ')[0]

def get_default_department():
    return Department.objects.get_or_create(name='БЕЗ ОТДЕЛА')[0]

def get_default_manger():
    return Department.objects.get_or_create(name='НЕ ПРИВЯЗАНО')[0]

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def month_choices():
    return [(r, r) for r in range(1, 13)]

def current_month():
    return datetime.date.today().month


class Sku(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)
    code = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sku'
        verbose_name = 'SKU'
        verbose_name_plural = 'SKU'


class SkuDirty(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)
    sku = models.ForeignKey(Sku, default=get_default_sku, on_delete=models.SET(get_default_sku))

    class Meta:
        db_table = 'sku_dirty'
        verbose_name = 'Dirty SKU'
        verbose_name_plural = 'Dirty SKU'


class DistributorGroup(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'distributor_group'
        verbose_name = 'Группа Дистрибьюторов'
        verbose_name_plural = 'Группы Дистрибьюторов'


class Distributor(models.Model):
    op_type = (
        ('Domestic', 'Domestic'),
        ('Export', 'Export'),
        ('ПРОВЕРИТЬ', 'ПРОВЕРИТЬ')
    )
    name = models.CharField(max_length=250, blank=False, unique=True)
    group = models.ForeignKey(DistributorGroup, null=True, on_delete=models.SET_NULL)
    operation_type = models.CharField(max_length=50, choices=op_type, blank=False, default='ПРОВЕРИТЬ')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'distributor'
        verbose_name = 'Дистрибьютор'
        verbose_name_plural = 'Дистрибьюторы'


class SOFile(models.Model):
    filename = models.CharField(max_length=250, blank=False, unique=True)
    upload = models.FileField(upload_to='so_files/')
    distributor = models.ForeignKey(Distributor, null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(choices=year_choices(), default=current_year)
    month = models.IntegerField(choices=month_choices(), default=current_month)
    is_month_inside = models.BooleanField(default=False)

    def __str__(self):
        return self.filename 

    class Meta:
        db_table = 'so_file'
        verbose_name = 'Файлы SO'
        verbose_name_plural = 'Файлы SO'

@receiver(post_delete, sender=SOFile)
def post_save_sofile(sender, instance, *args, **kwargs):
    """ Clean Old SO file """
    try:
        instance.upload.delete(save=False)
    except:
        pass


class Channel1(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel_1'
        verbose_name = 'Канал 1'
        verbose_name_plural = 'Канал 1'


class Channel2(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel_2'
        verbose_name = 'Канал 2'
        verbose_name_plural = 'Канал 2'


class Format1(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'format_1'
        verbose_name = 'Формат 1'
        verbose_name_plural = 'Формат 1'


class Format2(models.Model):
    name = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'format_2'
        verbose_name = 'Формат 2'
        verbose_name_plural = 'Формат 2'


class Manager(models.Model):
    name = models.CharField(max_length=250, blank=False, )

    def __str__(self):
        return self.filename 

    class Meta:
        db_table = 'manager'
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Department(models.Model):
    name = models.CharField(max_length=50, blank=False)
    team = models.CharField(max_length=50, blank=False, unique=True)
    manager = models.ManyToManyField(Manager, through='ManagerDepartments', related_name='departments')

    def __str__(self):
        return self.team

    class Meta:
        db_table = 'department'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class ManagerDepartments(models.Model):

    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_head = models.BooleanField()

    class Meta:
        db_table = 'manager_department'


class Shop(models.Model):
    db_code = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=250, blank=False)
    distributor = models.ForeignKey(Distributor, null=False, on_delete=models.CASCADE)
    channel_1 = models.ForeignKey(Channel1, default=get_default_channel1, on_delete=models.SET(get_default_channel1))
    channel_2 = models.ForeignKey(Channel2, default=get_default_channel2, on_delete=models.SET(get_default_channel2))
    format_1 = models.ForeignKey(Format1, default=get_default_format1, on_delete=models.SET(get_default_format1))
    format_2 = models.ForeignKey(Format2, default=get_default_format2, on_delete=models.SET(get_default_format2))
    manager = models.ForeignKey(Manager, default=get_default_manger, 
        on_delete=models.SET(get_default_manger))

    def __str__(self):
        return self.filename 

    class Meta:
        db_table = 'shop'
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        unique_together = ('name', 'address',)


#class Location(models.Model):
#    city = models.CharField(max_length=50, blank=False, unique=True)
#    region = models.CharField(max_length=50, blank=False)
#    country = models.CharField(max_length=50, blank=False)
#
#    class Meta:
#        db_table = 'location'
#        verbose_name = 'Локация'
#        verbose_name_plural = 'Локация'