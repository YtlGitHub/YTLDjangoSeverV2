# 后台管理子路由文件


from django.contrib import admin
from django.urls import path
from myadmin.views import index


urlpatterns = [
    path('<int:n>/', index.index, name="myadmin_index"),
    path('iframe/<int:n>/', index.iframe, name="iframe"),
    path('pagesIframe/<int:dashboard>/<int:n>/<int:pageNums>/', index.pages_iframe, name="pages_iframe"),
    path('YTLUrl/<int:n>/', index.ytl_url, name="ytl_url"),
]
