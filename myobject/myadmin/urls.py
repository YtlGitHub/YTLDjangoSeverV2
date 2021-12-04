# 后台管理子路由文件


from django.contrib import admin
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import prototype
from myadmin.views import ytl


urlpatterns = [
    path('', index.index, name="myadmin_index"),  # 后台首页

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 浏览员工管理路由
    path('user/add', user.add, name="myadmin_user_add"),  # 添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),  # 删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 编辑
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 修改

    # 后台管理员登入、退出路由
    path('login', index.login, name="myadmin_login"),  # 加载登入表单
    path('dologin', index.dologin, name="myadmin_dologin"),  # 执行登入
    path('logout', index.logout, name="myadmin_logout"),  # 退出登入

    # 样机信息管理路由
    # path('prototype/all/', prototype.all_prototype, name="myadmin_prototype_all"),  # 展示全部信息
    path('prototype/pages/<int:n>/<int:pageNums>/', prototype.pages_prototype, name="myadmin_prototype_pages"),  # 分页展示信息
    path('prototype/add', prototype.add, name="myadmin_prototype_add"),  # 添加表单
    path('prototype/insert', prototype.insert, name="myadmin_prototype_insert"),  # 执行添加
    path('prototype/del/<int:uid>', prototype.delete, name="myadmin_prototype_delete"),  # 删除
    path('prototype/edit/<int:uid>', prototype.edit, name="myadmin_prototype_edit"),  # 编辑
    path('prototype/update/<int:uid>', prototype.update, name="myadmin_prototype_update"),  # 修改
    path('prototype/editUserName/<int:uid>', prototype.edit_user_name, name="myadmin_prototype_edit_user_name"),  # 只编辑名字
    path('prototype/updateUserName/<int:uid>', prototype.update_user_name, name="myadmin_prototype_update_user_name"),  # 只修改名字

    # ytl信息管理路由
    path('YTLUrl/', ytl.ytl_url, name="myadmin_ytl_ytl_url"),  # 我的常用网址
    path('phoneInfo/', ytl.phone_info, name="myadmin_ytl_phone_info"),  # adb命令查看手机信息
    path('classNameimgs/', ytl.class_name_imgs, name="myadmin_ytl_class_name_imgs"),  # adb命令查看手机信息
]
