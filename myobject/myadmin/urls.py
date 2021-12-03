# 后台管理子路由文件


from django.contrib import admin
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import prototype
from myadmin.views import ytl


urlpatterns = [
    path('<int:n>/', index.index, name="myadmin_index"),  # 后台首页

    # 员工信息管理路由
    path('', user.index0, name="myadmin_user_index0"),  # 后台首页
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
    path('iframe/', prototype.iframe, name="myadmin_prototype_iframe"),  # 展示全部信息
    path('pagesIframe/<int:n>/<int:pageNums>/', prototype.pages_iframe, name="myadmin_prototype_pages_iframe"),  # 分页展示信息
    # path('iframe/<int:n>/', index.iframe, name="iframe"),  # 展示全部信息
    # path('pagesIframe/<int:dashboard>/<int:n>/<int:pageNums>/', index.pages_iframe, name="pages_iframe"),  # 分页展示信息

    # ytl信息管理路由
    path('YTLUrl/', ytl.ytl_url, name="myadmin_ytl_ytl_url"),  # 我的常用网址
    path('phoneInfo/', ytl.phone_info, name="myadmin_ytl_phone_info"),  # adb命令查看手机信息

    path('YTLUrl/<int:n>/', index.ytl_url, name="ytl_url"),  # 我的常用网址
    path('phoneInfo/<int:n>', index.phone_info, name="phone_info"),  # adb命令查看手机信息
]
