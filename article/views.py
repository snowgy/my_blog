from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse


# Create your views here.


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, article_id):
    try:
        post = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    dates = Article.objects.datetimes('date_time', 'month', order='DESC')
    return render(request, 'archives.html', {'dates': dates})


def time_year(request, year):
    post_list = Article.objects.filter(date_time__year=year)
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'archieve.html', {'post_list': post_list})


def time_month(request, year, month):
    post_list = Article.objects.filter(date_time__year=year, date_time__month=month)
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'archieve.html', {'post_list': post_list})


def about_me(request):
    return render(request, 'about_me.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archieve.html', {'post_list': post_list,
                                                         'error': True})
            else:

                return render(request, 'archieve.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


def item_pubdate(item):
    return item.add_date


class RssFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


def topic(request):
    tags = set()
    posts = Article.objects.all()
    for post in posts:
        tags.add(post.category)

    return render(request, 'topic.html', {'tags': tags})
