# ytl信息管理的视图文件
from django.shortcuts import render


def ytl_url(request):
    '''我的常用网址'''
    context = {"myadmin_ytl_menu_open": "menu-open", "myadmin_ytl_ytl_url_active": "active"}
    return render(request, "myadmin/ytl/YTLURL.html", context)


def phone_info(request):
    '''adb命令查看手机信息'''
    context = {"myadmin_ytl_menu_open": "menu-open", "myadmin_ytl_phone_info_active": "active"}
    return render(request, "myadmin/ytl/phoneInfo.html", context)


def class_name_imgs(request):
    return render(request, "myadmin/ytl/classNameimgs.html")
