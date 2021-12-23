# 违规记录信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import *
from itertools import chain  # 导入不同对象链接到一起函数
from django.core.paginator import Paginator  # 导入分页器
# from django.db.models import Sum  # 导入求和函数
from django.contrib import messages  # 导入提示信息模块
from django.shortcuts import redirect  # 导入重定向
from django.urls import reverse  # 导入重定向


def discipline(request, n=1, pageNums=5):
  '''分页浏览信息'''
  pName = Discipline
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
  dlist = p.page(n)  # 当前的页
  userAll = User.objects.all()
  context = {"disciplineList": dlist,
             "n": n,
             "pagelist": p.page_range,
             "pnumpages": p.num_pages,
             "mywhere": mywhere,
             "pCount": pCount,
             "pagesNum": pageNums,
             "myadmin_discipline_menu_open": "menu-open",
             "myadmin_discipline_active": "active",
             "userAllList": userAll,
             # "idName": idName,
             # "userName": userName,
             }
  # print(Dashboard)
  return render(request, "myadmin/discipline/discipline.html", context)


def insert(request):
  '''执行信息添加'''
  try:
    ob = Discipline()
    ob.name = request.POST['name']  # 姓名
    ob.job_number = request.POST['job_number']  # 工号
    ob.supplier = request.POST['supplier']  # 部门
    ob.violation = request.POST['violation']  # 记录
    ob.time = request.POST['time']  # 时间
    ob.actual = request.POST['actual']  # 实际
    ob.fine = request.POST['fine']  # 是否罚款
    ob.money = request.POST['money']  # 罚款金额
    ob.save()
    context = {'info': '添加成功'}
    messages.info(request, '添加成功!')
  except Exception as err:
    print(err)
    context = {'info': '添加失败'}
    messages.info(request, '添加失败')
  # return render(request, "myadmin/info.html", context)
  return redirect(reverse("myadmin_discipline", kwargs={"n": 1, "pageNums": 5}))


def update(request, uid=1):
  '''执行信息编辑'''
  try:
    ob = Discipline.objects.get(id=uid)
    ob.name = request.POST['name']  # 姓名
    ob.job_number = request.POST['job_number']  # 工号
    ob.supplier = request.POST['supplier']  # 部门
    ob.violation = request.POST['violation']  # 记录
    ob.time = request.POST['time']  # 时间
    ob.actual = request.POST['actual']  # 实际
    ob.fine = request.POST['fine']
    ob.money = request.POST['money']
    ob.save()
    context = {'info': '修改成功'}
    messages.info(request, '修改成功!')
  except Exception as err:
    print(err)
    context = {'info': '修改失败'}
    messages.info(request, '修改失败')
  # return render(request, "myadmin/info.html", context)
  return redirect(reverse("myadmin_discipline", kwargs={"n": 1, "pageNums": 5}))