from django.shortcuts import render
from django.http import JsonResponse  # 导入ajax传参模块
from myadmin.models import *
from myadmin.views.prototype import storage_prototype
from django.contrib import messages  # 导入只提示一次的模块


def ytl_ajax(request):
  '''转借视图'''
  if request.method == 'POST':
    # prototypeId = request.POST.get('prototypeId')
    remarks = request.POST.get('remarks')  # 备注
    idNumber = request.POST.get('idNumber')  # id号
    userName = request.POST.get('userName')  # 用户名
    '''执行转借信息编辑'''
    try:
      ob = PrototypeInfo.objects
      ob = ob.get(id=idNumber)
      ob.user_name = userName
      ob.borrow_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      ob.备注 = remarks
      ob.save()
      # 把样机表信息存储在session中
      storage_prototype(request)
      context = {'info': '转借成功', 'userName': userName, 'remarks': remarks}
    except Exception as err:
      print(err)
      context = {'info': '转借失败'}
    print("ajax", remarks, idNumber)
    return JsonResponse(context)
  return render(request, "myweb/infoFront.html")


def ytl_ajax_still_time(request):
  '''归还视图'''
  if request.method == 'POST':
    idNumber = request.POST.get('idNumber')  # id号
    '''执行确认归还'''
    try:
      ob = PrototypeInfo.objects
      ob = ob.get(id=idNumber)
      ob.user_name = "谭华杰"
      stillTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      ob.still_time = stillTime
      ob.save()
      # 把样机表信息存储在session中
      storage_prototype(request)
      context = {'info': '归还成功', 'userName': "谭华杰", "stillTime": stillTime}
    except Exception as err:
      print(err)
      context = {'info': '归还失败'}
    print("ajax", idNumber)
    return JsonResponse(context)