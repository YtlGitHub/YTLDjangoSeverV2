# ytl信息管理的视图文件
from django.shortcuts import render


def ytl_url(request, n=1):
    '''我的常用网址'''
    return render(request, "myadmin/ytl/YTLURL.html")


def phone_info(request, n=1):
    '''adb命令查看手机信息'''
    return render(request, "myadmin/ytl/phoneInfo.html")


def class_name_imgs(request):
    return render(request, "myadmin/ytl/classNameimgs.html")
