"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from custom_auth import urls as custom_auth_urls
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ua/', include(custom_auth_urls, namespace='custom_auth')),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^blog/new/', views.new_post, name='new_post'),
    url(r'^blog/(?P<post_id>[0-9]+)/update', views.update_post, name='update_post'),
    url(r'^blog/(?P<post_id>[0-9]+)/saved', views.update_post_save, name='update_post_save'),
    url(r'^blog/admin/', views.admin_post, name='admin_post'),
    url(r'^blog/Save/', views.new_post_save, name='new_post_save'),
    url(r'^blog/post/(?P<post_id>[0-9]+)', views.post_details, name='post_details'),
    url(r'^blog/list/', views.get_post_list, name='post_list'),
    url(r'^blog/(?P<post_id>[0-9]+)/delete', views.delete_post, name='update_post'),
]
