from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("欢迎进入会员移动点餐端！")re
    return render(request, "mobile/index/index.html")
