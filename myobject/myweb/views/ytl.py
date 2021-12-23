# ytl信息管理的视图文件
from django.shortcuts import render


def ytl_url(request):
    '''我的常用网址'''
    context = {"myweb_ytl_ytl_url_menu_open": "menu-open", "myweb_ytl_ytl_url_active": "active"}
    return render(request, "myweb/ytl/YTLURL.html", context)


def phone_info(request):
    '''adb命令查看手机信息'''
    context = {"myweb_ytl_phone_info_menu_open": "menu-open", "myweb_ytl_phone_info_active": "active"}
    return render(request, "myweb/ytl/phoneInfo.html", context)


def modal(request):
    context = {"myweb_ytl_phone_info_menu_open": "menu-open", "myweb_ytl_modal_active": "active"}
    return render(request, "myweb/ytl/modal.html", context)


def text(request):
    print("测试用")
