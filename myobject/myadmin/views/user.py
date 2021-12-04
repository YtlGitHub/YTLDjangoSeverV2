# 员工信息管理的视图文件
from django.shortcuts import render
from django.shortcuts import redirect  # 导入重定向函数
from django.urls import reverse  # 导入重定向函数
from django.http import HttpResponse
from myadmin.models import *
from datetime import datetime
from django.core.paginator import Paginator  # 导入分页模块
from django.db.models import Q


def index(request, pIndex=1):
    '''浏览信息'''
    umod = User.objects
    ulist = umod.filter(status__lt=9)  # 查询状态小于9的数据
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw) | Q(status__contains=kw))
        mywhere.append("keyword="+kw)
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)  # 以每2条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex < 1:
        pIndex = 1
    elif pIndex > maxpages:
        pIndex = maxpages
    list2 = page.page(pIndex)  # 获取当前页数据
    plits = page.page_range  # 获取页码列表信息
    usercount = page.count
    context = {"userlist": list2, "plist": plits, "pIndex": pIndex, "maxpages": maxpages, "mywhere": mywhere, "usercount": usercount}
    return render(request, 'myadmin/user/index.html', context)


def add(request):
    '''加载信息添加表单'''
    return render(request, 'myadmin/user/add.html')


def insert(request):
    '''执行信息添加'''
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        password = request.POST['password']
        retypePassword = request.POST['retype_password']
        if password and retypePassword:
            if password == retypePassword:
                import hashlib, random
                md5 = hashlib.md5()
                n = random.randint(100000, 999999)
                s = request.POST['password']+str(n)  # 从表单中获取密码并添加干扰值
                md5.update(s.encode('utf-8'))  # 蒋要产生md5的字符串放进去
                ob.password_hash = md5.hexdigest()  # 获取md5值
                print("insert", md5.hexdigest())
                ob.password_salt = n
                ob.status = 1
                ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ob.save()
                context = {'info': '添加成功'}
            else:
                context = {'info': '添加失败 两次密码不一致'}
        else:
            context = {'info': '添加失败 输入为空'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败'}
    return render(request, "myadmin/info.html", context)


def delete(request, uid=1):
    '''执行信息删除'''
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '删除成功'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败'}
    return render(request, "myadmin/info.html", context)


def edit(request, uid=1):
    '''加载信息编辑表单'''
    #try:
    ob = User.objects.get(id=uid)
    context = {"user": ob}
    return render(request, 'myadmin/user/edit.html', context)
    #except Exception as err:
        # print(err)
        # context = {"info": "没有找到要修改的信息"}
        # return render(request, "myadmin/info.html", context)


def update(request, uid=1):
    '''执行信息编辑'''
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now()
        ob.save()
        context = {'info': '修改成功'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
    return render(request, "myadmin/info.html", context)
