# 样机信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import *
from itertools import chain  # 导入不同对象链接到一起函数
from django.core.paginator import Paginator  # 导入分页器
# from django.db.models import Sum  # 导入求和函数


# 把样机表信息存储在session中
def storage_prototype(request):
    # 获取用户id，用id获取用户信息，在写入到session中
    sessionusername = request.session["adminuser"]["username"]  # 获取session里面的用户名
    pusername = PrototypeInfo.objects  # 对session里面获取的名字在prototype_info样机表里面模糊查询，即对name字段进行包含查询
    request.session["prototype"] = {
        "prototypeCount": pusername.filter(user_name__contains=sessionusername).count(),
        "dedomestic": pusername.filter(user_name__contains=sessionusername, de__contains="内销").count(),
        "deexport": pusername.filter(user_name__contains=sessionusername, de__contains="外销").count(),
    }
    print('request.session', request.session["prototype"])


def pages_prototype(request, n=1, pageNums=5):
    '''分页浏览信息'''
    pName = PrototypeInfo
    idName = request.GET.get("id_name", "")
    userName = request.GET.get("user_name", "")
    de = request.GET.get("de", "")
    brand = request.GET.get("brand", "")
    pv = request.GET.get("pv", "")
    os = request.GET.get("os", "")
    IMEI = request.GET.get("IMEI", "")
    # "mywhere" 定义一个用于存储搜索条件的变量
    mywhere = f"?id_name={idName}&user_name={userName}&de={de}&brand={brand}&pv={pv}&os={os}&IMEI={IMEI}"  # 追加搜索条件
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
    context = {"prototypeList": plist,
               "n": n,
               "pagelist": p.page_range,
               "pnumpages": p.num_pages,
               "mywhere": mywhere,
               "pCount": pCount,
               "pagesNum": pageNums,
               # "idName": idName,
               # "userName": userName,
               }
    # print(Dashboard)
    return render(request, "myweb/prototype/pagesPrototype.html", context)


def delete(request, uid=1):
    '''执行信息删除还没写'''
    try:
        ob = PrototypeInfo.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        # 把样机表信息存储在session中
        storage_prototype(request)
        context = {'info': '删除成功'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败'}
    return render(request, "myweb/info.html", context)


def edit(request, uid=1):
    '''加载信息编辑表单'''
    try:
        ob = PrototypeInfo.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myweb/prototype/edit.html', context)
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息"}
        return render(request, "myweb/info.html", context)


def update(request, uid=1):
    '''执行信息编辑'''
    try:
        ob = PrototypeInfo.objects.get(id=uid)
        ob.id_name = request.POST['id_name']
        ob.de = request.POST['de']
        ob.brand = request.POST['brand']
        ob.pv = request.POST['pv']
        ob.os = request.POST['vos']
        ob.m_name = request.POST['m_name']
        ob.IMEI = request.POST['IMEI']
        ob.name = request.POST['name']
        ob.user_name = request.POST['user_name']
        ob.borrow_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.备注 = request.POST['remarks']
        ob.save()
        # 把样机表信息存储在session中
        storage_prototype(request)
        context = {'info': '修改成功'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败'}
    return render(request, "myweb/info.html", context)


def edit_user_name(request, uid=1):
    '''加载转借信息编辑表单'''
    # try:
    ob = PrototypeInfo.objects.get(id=uid)
    userAll = User.objects.all()
    context = {"user": ob, "userAllList": userAll}
    return render(request, 'myweb/prototype/editUserName.html', context)
    # except Exception as err:
    #     print(err)
    #     context = {"info": "没有找到要修改的信息"}
    #     return render(request, "myweb/info.html", context)


def update_user_name(request, uid=1):
    '''执行转借信息编辑'''
    try:
        ob = PrototypeInfo.objects
        ob = ob.get(id=uid)
        ob.user_name = request.POST['user_name']
        ob.borrow_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.备注 = request.POST['remarks']
        ob.save()
        # 把样机表信息存储在session中
        storage_prototype(request)
        context = {'info': '转借成功'}
    except Exception as err:
        print(err)
        context = {'info': '转借失败'}
    return render(request, "myweb/info.html", context)
