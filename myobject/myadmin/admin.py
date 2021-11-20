from django.contrib import admin
from myadmin.models import *
# Register your models here.


# admin.site.register(Material)


@admin.register(PrototypeInfo)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(PrototypeHzx)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(PrototypeJxl)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypeztw)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypewjy)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypelzx)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypepyc)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypexth)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypehwp)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Prototypelkx)
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'id_name', 'de', 'brand', 'pv', 'os', 'm_name', 'IMEI', 'name', 'user_name', 'borrow_time', 'still_time', '备注')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'id_name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    list_editable = ['备注', ]  # 设置可编辑字段


@admin.register(Material)  # 物料记录
class PrototypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'name', 'material', 'gave_time', 'sum')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # drdering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    # list_editable = ['sum', ]  # 设置可编辑字段


@admin.register(Discipline)  # 违规记录
class PrototypeAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id', 'name', 'job_number', 'supplier', 'violation', 'time', 'actual','fine', 'money')
    # 设置那些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')
    # list_per_page: 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序
    # list_editable = ['sum', ]  # 设置可编辑字段