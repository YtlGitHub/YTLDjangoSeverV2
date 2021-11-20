# 前台大堂点餐子路由文件


from django.urls import path
from myweb.views import index


urlpatterns = [
    path('', index.index, name="myweb_index"),
]

