# 自定义中间件（执行是否登入判断）
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
import re
from myadmin.models import PrototypeInfo


class ShopMiddleware:
    def __init__(self, get_response):  # 魔术方法，用来初始化类对象的，只在启动服务的时候调用一次
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):  # 中间件执行的时候必须调用的方法，每次请求的时候都会调用
        path = request.path
        print("url:", path)

        # 判断前台以prototype开头的要做登入判断
        if re.match(r'^/prototype', path):
            # 判断是否登入(在session中没有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登入页
                return redirect(reverse("myweb_login"))

        # 判断管理后台是否登入
        # 定义后台不登入也可直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin']
        # 判断当前请求url地址是否以myadmin开头,并且不再urllist中，才做是否登入判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断是否登入(在session中没有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登入页
                return redirect(reverse("myadmin_login"))
            if request.session["adminuser"]["status"] != 6:  # 判断是否管理员状态为6的是管理员，如果不是重定向到提示页面
                # 重定向到提示页面
                context = {"info": "你不是管理员无法进入管理员页面"}
                return render(request, 'myweb/info.html', context)  # 登入后台管理员

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
