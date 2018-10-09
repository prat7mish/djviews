"""djviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import post_model_list_view,post_model_detail_view,post_model_create_view,post_model_update_view, post_model_delete_view

urlpatterns = [
    url(r'^$',post_model_list_view , name='list'),
    url(r'^create/$',post_model_create_view , name='create'),
    url(r'^(?P<id>\d+)/$',post_model_detail_view , name='detail'),
    url(r'^(?P<id>\d+)/delete/$',post_model_delete_view , name='delete'),
    url(r'^(?P<id>\d+)/edit/$',post_model_update_view , name='update'),


]
