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
from django.db.models import Q
from django.http import JsonResponse  # 导入ajax弹框模块


def discipline(request, n=1, pageNums=5):
  '''分页浏览信息'''
  dName = Discipline
  idName = request.GET.get("id_name", "")
  # "mywhere" 定义一个用于存储搜索条件的变量
  mywhere = f"?id_name={idName}"  # 追加搜索条件
  if idName != "":
    print(idName, "idName,有值")
    list = dName.objects.filter(Q(name__contains=idName) | Q(job_number__contains=idName) | Q(supplier__contains=idName) | Q(violation__contains=idName) | Q(time__contains=idName) | Q(actual__contains=idName) | Q(fine__contains=idName) | Q(money__contains=idName))  # 模糊 “|”或 查询
    # list = dName.objects.filter(Q(id_name__contains=idName) & Q(user_name__contains=userName))  # 模糊 “&”与 查询
    # list = dName.objects.filter(id_name__contains=idName, user_name__contains=userName)  # 模糊 “,”与 查询
  else:
    print("都没值")
    list = dName.objects.filter()
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
             "idName": idName,
             }
  return render(request, "myadmin/discipline/discipline.html", context)


def insert(request):
  '''执行信息添加'''
  # try:
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
  # except Exception as err:
  #   print(err)
  #   context = {'info': '添加失败'}
  #   messages.info(request, '添加失败')
  # return render(request, "myadmin/info.html", context)
  return redirect(reverse("myadmin_discipline", kwargs={"n": 1, "pageNums": 5}))


def update(request, uid=1):
  '''执行信息编辑'''
  # try:
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
  # except Exception as err:
  #   print(err)
  #   context = {'info': '修改失败'}
  #   messages.info(request, '修改失败')
  # return render(request, "myadmin/info.html", context)
  return redirect(reverse("myadmin_discipline", kwargs={"n": 1, "pageNums": 5}))


def delete(request):
    '''执行信息删除'''
    if request.method == "POST":
        idNumber = request.POST.get('idNumber')  # id号
        print("idNumber", idNumber)
        try:
            ob = Discipline.objects.get(id=idNumber)
            ob.delete()
            context = {'info': '删除成功'}
        except Exception as err:
            print(err)
            context = {'info': '删除失败'}
        print("违规记录删除信息")
        return JsonResponse(context)
