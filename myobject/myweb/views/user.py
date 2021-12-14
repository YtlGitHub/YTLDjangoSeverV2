# 前台员工信息的视图文件
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


def edit_personal(request, uid=1):
    '''加载个人信息编辑表单'''
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myweb/user/editPersonal.html', context)
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息"}
        return render(request, "myweb/info.html", context)


def update_personal(request, uid=1):
    '''执行个人信息编辑'''
    try:
        # 获取原图名字
        headPortraitName = request.POST["head_portrait"]
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
        ob.nickname = request.POST['nickname']  # 昵称
        ob.personal_signature = request.POST['personal-signature']  # 个性签名
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
    return render(request, "myweb/info.html", context)
