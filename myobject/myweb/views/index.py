from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("欢迎进入前台的大堂点餐端！<a></a>")
    return render(request, "myweb/index/index.html")
