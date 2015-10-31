# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse

from rest_framework import viewsets

from forms import NewPostForm
from models import Post
from serializers import PostSerializer


def index(request):
    context = {'home_page_data': 'Hello Django!'}
    return render(request, 'django_blog/index.html', context)


@login_required
def new_post(request):
    form = NewPostForm
    return render(request, 'django_blog/new_post.html', {'form': form})


@login_required
def admin_post(request):
    all_posts = Post.objects.all()
    return render(request, 'django_blog/admin_post.html', {'all_posts': all_posts})


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'django_blog/post_details.html', {'post': post})


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = NewPostForm(instance=post)
    return render(request, 'django_blog/update_post.html',
                  {
                      'form': form,
                      'post_id': post_id
                  })


def get_post_list(request):
    all_posts = Post.objects.all()
    data = serializers.serialize('json', all_posts)
    return HttpResponse(data)


@login_required
def new_post_save(request):
    if request.method == 'POST':
        create_new_post = Post(create_date=timezone.now(), author_id=request.user)
        form = NewPostForm(request.POST, instance=create_new_post)
        if form.is_valid():
            form.save()
            return render(request, 'django_blog/admin_post.html',
                          {
                              'form': form,
                              'success_msg': 'پست جدید در سیستم ثبت شد'
                          })
        else:
            return render(request, 'django_blog/new_post.html',
                          {
                              'form': form,
                              'error_msg': 'لطفا فیلدهای الزامی را پر کنید'
                          })
    else:
        form = NewPostForm()
        return render(request, 'django_blog/new_post.html', {'form': form})


@login_required
def update_post_save(request, post_id):
    if request.method == 'POST':
        post_for_update = get_object_or_404(Post, pk=post_id)
        form = NewPostForm(request.POST, instance=post_for_update)
        if form.is_valid():
            form.save()
            return render(request, 'django_blog/admin_post.html',
                          {
                              'form': form,
                              'success_msg': 'پست مورد نظر ویرایش شد'
                          })
        else:
            return render(request, 'django_blog/update_post.html',
                          {
                              'form': form,
                              'error_msg': 'لطفا فیلدهای الزامی را پر کنید'
                          })
    else:
        form = NewPostForm()
        return render(request, 'django_blog/update_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return render(request, 'django_blog/admin_post.html',
                  {
                      'success_msg': 'پست مورد نظر حذف شد'
                  })


class PostViewSet(viewsets.ModelViewSet):
    all_post = Post.objects.all()
    queryset = all_post
    serializer_class = PostSerializer
