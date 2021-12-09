# 前台大堂点餐子路由文件


from django.urls import path
from myweb.views import index
from myweb.views import prototype
from myweb.views import user


urlpatterns = [
    # 首页浏览
    path('', index.index_front, name="myweb_index_front"),
    path('prototype/index', index.index, name="myweb_index"),

    # 员工信息管理路由
    path('prototype/user/editPersonal/<int:uid>', user.edit_personal, name="myweb_user_edit_personal"),  # 只能编辑个人信息，不能编辑他人信息路由
    path('prototype/user/updatePersonal/<int:uid>', user.update_personal, name="myweb_user_update_personal"),  # 执行修改个人信息路由

    # 后台管理员登入、退出路由
    path('isAdmin/', index.is_admin, name="myweb_is_admin"),  # 判断是否管理员账号
    path('login/', index.login, name="myweb_login"),  # 加载登入表单
    path('dologin/', index.dologin, name="myweb_dologin"),  # 执行登入
    path('logout/', index.logout, name="myweb_logout"),  # 退出登入
    
    # 样机信息管理路由
    path('prototype/pages/<int:n>/<int:pageNums>/', prototype.pages_prototype, name="myweb_prototype_pages"),  # 分页展示信息
    path('prototype/del/<int:uid>', prototype.delete, name="myweb_prototype_delete"),  # 删除
    path('prototype/edit/<int:uid>', prototype.edit, name="myweb_prototype_edit"),  # 编辑表单
    path('prototype/update/<int:uid>', prototype.update, name="myweb_prototype_update"),  # 执行编辑修改信息
    path('prototype/editUserName/<int:uid>', prototype.edit_user_name, name="myweb_prototype_edit_user_name"),  # 只能编辑自己名字表单
    path('prototype/updateUserName/<int:uid>', prototype.update_user_name, name="myweb_prototype_update_user_name"),  # 执行只能编辑修改自己名字
]

