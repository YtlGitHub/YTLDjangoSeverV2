from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myadmin.models import User
from django.shortcuts import redirect
from django.urls import reverse
from myweb.views.prototype import storage_prototype  # 导入自定义的函数(把样机信息存储在session)
from myweb.views.user import storage_user  # 导入自定义的函数(把样机信息存储在session)


# 没登入展示的页面
def index_front(request):
    return render(request, "myweb/index/indexFront.html")


def index(request):
    # return HttpResponse("欢迎进入前台的大堂点餐端！<a></a>")
    storage_prototype(request)  # 样机信息写入session调用在主页就可以显示最新的数据了
    storage_user(request)  # 用户信息写入session调用在主页就可以显示最新的数据了
    return render(request, "myweb/index/index.html")


# 判断是否管理员账号
def is_admin(request):
    try:
        ustatus = request.session["adminuser"]["status"]
        print("ustatus", ustatus)
        if ustatus == 6:
            return redirect(reverse("myadmin_index"))
        else:
            context = {"info": "你不是管理员无法进入管理员页面"}
            return render(request, 'myweb/info.html', context)  # 登入后台管理员
    except Exception as err:
        print(err)
    context = {"info": "请先登录", "login": "登录", "loginAdmin": "登录后台"}
    return render(request, 'myweb/infoFront.html', context)  # 登入后台管理员


# 员工登入表单
def login(request):
    return render(request, 'myweb/index/login.html')


# 执行员工登入
def dologin(request):
    # 根据登入账号获取登录者信息
    try:
        # 根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])
        # 判断当前用户是否管理员
        if user.status == 1 or user.status == 6:  # 状态为1正常或者状态为6管理员可正常登入
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
                return redirect(reverse("myweb_index"))
            else:
                context = {"info": "登录密码错误！"}
        else:
            context = {"info": "无效的登录账号！"}
    except Exception as err:
        print(err)
        context = {"info": "登录账号不存在"}
    return render(request, 'myweb/index/login.html', context)


# 管理员退出
def logout(request):
    del request.session["adminuser"]
    return redirect(reverse("myweb_login"))
