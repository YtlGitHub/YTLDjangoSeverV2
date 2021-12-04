from django.shortcuts import render
from django.http import HttpResponse
# from myadmin.models import *
from myadmin.models import User, PrototypeInfo
# Create your views here.
from datetime import datetime  # 导入时间
from django.core.paginator import Paginator  # 导入分页器
from django.db.models import Q # 导入 &与 |或 模糊查询
from itertools import chain  # 导入不同对象链接到一起函数
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    '''首页'''
    return render(request, f'myadmin/index/index.html')


# 管理员登入表单
def login(request):
    return render(request, 'myadmin/index/login.html')


# 执行管理员登入
def dologin(request):
    # 根据登入账号获取登录者信息
    try:
        # 根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])
        # 判断当前用户是否管理员
        if user.status == 6:
            # 判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['password']+user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 蒋要产生md5的字符串放进去
            if user.password_hash == md5.hexdigest():  # 获取md5值
                print("dologin", md5.hexdigest())
                # 蒋当前登入成功的用户信息以adminuser为key写入到session中
                request.session["adminuser"] = user.toDict()
                # 重定向到后台管理页面
                return redirect(reverse("myadmin_index"))
            else:
                context = {"info": "登录密码错误！"}
        else:
            context = {"info": "无效的登录账号！"}
    except Exception as err:
        print(err)
        context = {"info": "登录账号不存在"}
    return render(request, 'myadmin/index/login.html', context)


# 管理员退出
def logout(request):
    del request.session["adminuser"]
    return redirect(reverse("myadmin_login"))

