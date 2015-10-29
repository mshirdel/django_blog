from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'home_page_data': 'Hello Django!'}
    return render(request, 'django_blog/index.html', context)


@login_required
def new_post(request):
    return render(request, 'django_blog/new_post.html')


@login_required
def admin_post(request):
    return render(request, 'django_blog/admin_post.html')
