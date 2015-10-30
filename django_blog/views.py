# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse

from forms import NewPostForm
from models import Post


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
