# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    return render(request, 'django_blog/admin_post.html')


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
