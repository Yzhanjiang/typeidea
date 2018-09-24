# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  django.core.paginator import  Paginator,EmptyPage
from django.db import connection
from django.http import HttpResponse, Http404
from  django.views.generic import ListView,DetailView


# Create your views here.

from .models import Post,Tag,Category
from  config.models import SideBar
from  comment.models import Comment


#CBV

class CommonMixin:
    def get_category_context(self):
        categories = Category.objects.filter(status=1)
        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        return  {
                'cav_cates':nav_cates,
                'cates':cates,
                 }

    def get_side_bars(self):
        return SideBar.objects.filter(status=1)

    def get_context_data(self,*args,**kwargs):
        side_bars = SideBar.objects.filter(status=1)
        recently_posts = Post.objects.filter(status=1)[:10]
        # hot_posts = Post.objects.filter(status=1).order_by('views')
        recently_comments = Comment.objects.filter(status=1)[:10]

        print(connection.queries)
        kwargs = {
            'side_bars': side_bars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
        }
        # context.update(extra_context)
        # return context
        kwargs.update(self.get_category_context())
        print(kwargs)
        return  super(CommonMixin,self).get_context_data(**kwargs)


class BasePostsView(CommonMixin,ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name =  'posts'
    paginate_by = 3
    allow_empty = True


class IndexView(BasePostsView):
    # def get(self,requset,*args,**kwargs):
        pass


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView,self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id= cate_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs('tag')
        try :
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return  []

        posts =  tag.posts.all()
        return posts


class PostView(CommonMixin,DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    print(context_object_name)


















#FUNC


def get_common_context():
    categories = Category.objects.filter(status=1)
    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')
    recently_comments = Comment.objects.filter(status=1)[:10]

    print(connection.queries)
    context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
        }
    return context

def post_list(request,category_id=None,tag_id=None):
    queryset = Post.objects.all()
    page = request.GET.get('page',1)
    page_size = 2
    try:
        page = int(page)
    except ValueError:
        page = 1
    if category_id :
        queryset = queryset.filter(category_id= category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset =[]
        else:
            queryset = tag.post.all()
            # queryset = tag.post_set.all()
    else:
        pass

    paginator = Paginator(queryset,page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # categories = Category.objects.filter(status=1)
    # nav_cates = []
    # cates = []
    # for cate in categories:
    #     if cate.is_nav:
    #         nav_cates.append(cate)
    #     else:
    #         cates.append(cate)
    #
    # side_bars = SideBar.objects.filter(status=1)
    #
    # recently_posts = Post.objects.filter(status=1)[:10]
    # # hot_posts = Post.objects.filter(status=1).order_by('views')
    # recently_comments = Comment.objects.filter(status=1)[:10]
    #
    # print(len(posts))
    # print(connection.queries)

    context = {
        'posts':posts,
    }

    common_context = get_common_context()
    context.update(common_context)
    return render(request,'blog/list.html',context=context)

def post_detail(request,pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("post does not exist")

    context = {
        'post': post,
    }
    common_context = get_common_context()
    context.update(common_context)

    return render(request, 'blog/detail.html', context=context)