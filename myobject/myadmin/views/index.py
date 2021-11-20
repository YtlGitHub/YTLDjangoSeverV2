from django.shortcuts import render
from django.http import HttpResponse
# from myadmin.models import *
from myadmin.models import PrototypeInfo, PrototypeHzx, PrototypeJxl, Prototypeztw, Prototypewjy, Prototypelzx, Prototypepyc, Prototypexth, Prototypehwp, Prototypelkx
# Create your views here.
from datetime import datetime  # 导入时间
from django.core.paginator import Paginator  # 导入分页器
from django.db.models import Q # 导入 &与 |或 模糊查询
from itertools import chain  # 导入不同对象链接到一起


def index(request, n=1):
    # return HttpResponse("欢迎进入点餐系统的后台管理！")
    base = f"myadmin/base{n}.html"
    context = {"base": base, }
    return render(request, f'myadmin/index/index{n}.html', context)


def iframe(request, n=1):
    # return HttpResponse("欢迎进入点餐系统的后台管理！")
    plist1 = PrototypeInfo.objects.all()
    plist2 = PrototypeHzx.objects.all()
    plist3 = PrototypeJxl.objects.all()
    plist5 = Prototypeztw.objects.all()
    plist6 = Prototypewjy.objects.all()
    plist7 = Prototypelzx.objects.all()
    plist8 = Prototypepyc.objects.all()
    plist9 = Prototypexth.objects.all()
    plist10 = Prototypehwp.objects.all()
    plist11 = Prototypelkx.objects.all()
    # plist = plist1 | plist2
    plist = chain(plist1, plist2, plist3, plist5, plist6, plist7, plist8, plist9, plist10, plist11)
    base = f"myadmin/base{n}.html"
    context = {"prototypeList": plist,
               "base": base,
               }
    return render(request, f"myadmin/index/iframe.html", context)


def pages_iframe(request, dashboard=1, n=1, pageNums=5):
    prototypeName = request.GET.get("prototypeName", "")
    print(prototypeName)
    if prototypeName == "杨天龙":
        pName = PrototypeInfo
    elif prototypeName == "何振兴":
        pName = PrototypeHzx
    elif prototypeName == "蒋小丽":
        pName = PrototypeJxl
    elif prototypeName == "郑廷威":
        pName = Prototypeztw
    elif prototypeName == "王杰玉":
        pName = Prototypewjy
    elif prototypeName == "刘志霞":
        pName = Prototypelzx
    elif prototypeName == "彭雨超":
        pName = Prototypepyc
    elif prototypeName == "许天华":
        pName = Prototypexth
    elif prototypeName == "黄伟鹏":
        pName = Prototypehwp
    elif prototypeName == "刘康欣":
        pName = Prototypelkx
    else:
        plist1 = PrototypeInfo.objects.all()
        plist2 = PrototypeHzx.objects.all()
        plist3 = PrototypeJxl.objects.all()
        plist5 = Prototypeztw.objects.all()
        plist6 = Prototypewjy.objects.all()
        plist7 = Prototypelzx.objects.all()
        plist8 = Prototypepyc.objects.all()
        plist9 = Prototypexth.objects.all()
        plist10 = Prototypehwp.objects.all()
        plist11 = Prototypelkx.objects.all()
        plistAll = chain(plist1, plist2, plist3, plist5, plist6, plist7, plist8, plist9, plist10, plist11)
        # plistAll = plist1 | plist2 | plist3 | plist4 | plist5 | plist6 | plist7 | plist8 | plist9 | plist10 | plist11
        pName = PrototypeInfo
    idName = request.GET.get("id_name", "")
    userName = request.GET.get("user_name", "")
    de = request.GET.get("de", "")
    brand = request.GET.get("brand", "")
    pv = request.GET.get("pv", "")
    os = request.GET.get("os", "")
    IMEI = request.GET.get("IMEI", "")
    # "mywhere" 定义一个用于存储搜索条件的变量
    mywhere = f"?prototypeName={prototypeName}&id_name={idName}&user_name={userName}&de={de}&brand={brand}&pv={pv}&os={os}&IMEI={IMEI}"  # 追加搜索条件
    if userName != "" and idName != "":
        print(idName, userName, "idName,userName,有值")
        # list = PrototypeInfo.objects.filter(Q(id_name__contains=idName) | Q(user_name__contains=userName))  # 模糊 “|”或 查询
        # list = PrototypeInfo.objects.filter(Q(id_name__contains=idName) & Q(user_name__contains=userName))  # 模糊 “&”与 查询
        list = pName.objects.filter(id_name__contains=idName, user_name__contains=userName)  # 模糊 “,”与 查询
    elif userName != "" and de != "":
        list = pName.objects.filter(user_name__contains=userName, de__contains=de)  # 模糊 “,”与 查询
    elif userName != "" and brand != "":
        list = pName.objects.filter(user_name__contains=userName, brand__contains=brand)  # 模糊 “,”与 查询
    elif userName != "" and pv != "":
        list = pName.objects.filter(user_name__contains=userName, pv__contains=pv)  # 模糊 “,”与 查询
    elif userName != "" and os != "":
        list = pName.objects.filter(user_name__contains=userName, os__contains=os)  # 模糊 “,”与 查询
    elif de != "" and brand != "":
        list = pName.objects.filter(de__contains=de, brand__contains=brand)  # 模糊 “,”与 查询
    elif de != "" and pv != "":
        list = pName.objects.filter(de__contains=de, pv__contains=pv)  # 模糊 “,”与 查询
    elif de != "" and os != "":
        list = pName.objects.filter(de__contains=de, os__contains=os)  # 模糊 “,”与 查询
    elif brand != "" and os != "":
        list = pName.objects.filter(brand__contains=brand, os__contains=os)  # 模糊 “,”与 查询
    elif brand != "" and pv != "":
        list = pName.objects.filter(brand__contains=brand, pv__contains=pv)  # 模糊 “,”与 查询
    elif idName != "":
        list = pName.objects.filter(id_name__contains=idName)  # 模糊查询，即对name字段进行包含查询
    elif userName != "":
        list = pName.objects.filter(user_name__contains=userName)  # 模糊查询，即对name字段进行包含查询
    elif de != "":
        list = pName.objects.filter(de__contains=de)  # 模糊查询，即对name字段进行包含查询
    elif brand != "":
        list = pName.objects.filter(brand__contains=brand)  # 模糊查询，即对name字段进行包含查询
    elif pv != "":
        list = pName.objects.filter(pv__contains=pv)  # 模糊查询，即对name字段进行包含查询
    elif os != "":
        list = pName.objects.filter(os__contains=os)  # 模糊查询，即对name字段进行包含查询
    elif IMEI != "":
        list = pName.objects.filter(IMEI__contains=IMEI)  # 模糊查询，即对name字段进行包含查询
    else:
        print("都没值")
        list = pName.objects.filter()
    p = Paginator(list, pageNums)  # 以pageNums条数据一页实例化分页对象
    pCount = p.count  # 总的条数
    # 判断页码值n是否有效
    if n < 1:
        n = 1
    elif n > p.num_pages:
        n = p.num_pages
    plist = p.page(n)  # 当前的页
    base = f"myadmin/base{dashboard}.html"
    context = {"prototypeList": plist,
               "dashboard": dashboard,
               "n": n,
               "pagelist": p.page_range,
               "pnumpages": p.num_pages,
               "mywhere": mywhere,
               "pCount": pCount,
               "pagesNum": pageNums,
               "prototypeName": prototypeName,
               "base": base,
               # "idName": idName,
               # "userName": userName,
               }
    # print(Dashboard)
    return render(request, "myadmin/index/pagesIframe.html", context)


def ytl_url(request, n=1):
    base = f"myadmin/base{n}.html"
    context = {"base": base, }
    return render(request, "myadmin/ytlgs/YTLURL.html", context)
