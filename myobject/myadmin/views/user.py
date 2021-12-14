# 员工信息管理的视图文件
from django.shortcuts import render
from django.shortcuts import redirect  # 导入重定向函数
from django.urls import reverse  # 导入重定向函数
from django.http import HttpResponse
from myadmin.models import *
from datetime import datetime
import os
from django.core.paginator import Paginator  # 导入分页模块
from django.db.models import Q
from PIL import Image  # 导入图片压缩模块


# 获取用户id，用id获取用户信息，再写入到session中---
def storage_user(request):
    uid = request.session["adminuser"]["id"]
    user = User.objects.get(id=uid)
    request.session["adminuser"] = user.toDict()


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
    page = Paginator(ulist, 5)  # 以每5条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex < 1:
        pIndex = 1
    elif pIndex > maxpages:
        pIndex = maxpages
    list2 = page.page(pIndex)  # 获取当前页数据
    plits = page.page_range  # 获取页码列表信息
    usercount = page.count
    context = {"userlist": list2, "plist": plits, "pIndex": pIndex, "maxpages": maxpages, "mywhere": mywhere, "usercount": usercount, "myadmin_user_index_active": "active"}
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
        ob.sex = request.POST['sex']
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
                # 获取用户id，用id获取用户信息，在写入到session中---
                storage_user(request)
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
        # 获取用户id，用id获取用户信息，在写入到session中---
        storage_user(request)
        context = {'info': '删除成功'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败'}
    return render(request, "myadmin/info.html", context)


def edit(request, uid=1):
    '''加载信息编辑表单'''
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/user/edit.html', context)
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息"}
        return render(request, "myadmin/info.html", context)


def update(request, uid=1):
    '''执行信息编辑'''
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now()
        ob.save()
        # 获取用户id，用id获取用户信息，在写入到session中---
        storage_user(request)
        context = {'info': '修改成功'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
    return render(request, "myadmin/info.html", context)


def edit_personal(request, uid=1):
    '''加载个人信息编辑表单'''
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/user/editPersonal.html', context)
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息"}
        return render(request, "myadmin/info.html", context)


def update_personal(request, uid=1):
    '''执行个人信息编辑'''
    try:
        # 获取原图名字
        headPortraitName = request.POST["head_portrait"]
        print("headPortraitName:", headPortraitName)
        # 先做图片上传处理
        myFile = request.FILES.get("pic", None)  # 获取头像信息
        print(myFile)
        if not myFile:
            fileName = headPortraitName
        else:
            fileName = str(datetime.now().strftime("%Y%m%d-%H%M%S")) + '.' + myFile.name.split('.').pop()
            destination = open(f"./static/uploads/user/headPortrait/{fileName}", "wb+")  # w读取b二进制，图片音频都属于二进制
            for chunk in myFile.chunks():  # 分块读取上传文件内容并写入目标文件
                destination.write(chunk)
            destination.close()  # 打开写入之后我们要关闭，用.close()这个方法关闭写入的文件
            # 执行图片缩放
            # im = Image.open("./static/uploads/user/headPortrait/"+fileName)
            # # 缩放到75*75(缩放后的宽高比例不变)
            # # im.thumbnail((75, 75))

            # # 设置屏幕分辨率(宽高一致)
            # out = im.resize((999, 999), Image.ANTIALIAS)
            # 第二个参数：
            # Image.NEAREST ：低质量
            # Image.BILINEAR：双线性
            # Image.BICUBIC ：三次样条插值
            # Image.ANTIALIAS：高质量

            # 把缩放后的图像用jpeg格式保存
            # out.save("./static/uploads/user/headPortrait/"+fileName, None)

        ob = User.objects.get(id=uid)
        ob.head_portrait = fileName  # 修改新的头像名字
        ob.nickname = request.POST['nickname']
        ob.personal_signature = request.POST['personal-signature']
        ob.update_at = datetime.now()
        ob.save()
        # 获取用户id，用id获取用户信息，在写入到session中---
        storage_user(request)
        context = {'info': '修改个人信息成功'}
        # 判断并删除老照片
        if myFile:
            try:
                os.remove(f"./static/uploads/user/headPortrait/{headPortraitName}")
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
        # 判断并删除新图片
        if myFile:
            try:
                os.remove(f"./static/uploads/user/headPortrait/{fileName}")
            except Exception as err:
                print(err)
    return render(request, "myadmin/info.html", context)
