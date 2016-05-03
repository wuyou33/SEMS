# author: HuYong
#coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from wechat import views,wechat_index,wechatViews


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="wechat/index.html")),
    url(r'^image',views.getimage),
    url(r'^regist$',views.regist),
    url(r'^doregist$',views.doregist),
    url(r'^dologin$',views.dologin),
    url(r'^wechat_index$',wechat_index.index),
    url(r'^bangding$',wechatViews.bangding),

]