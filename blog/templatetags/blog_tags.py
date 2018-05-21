# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-8


from django import template
from django.db.models import Count
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag   # 使用该装饰器定义以下函数为一个简单标签（simple_tag）并注册它
def total_posts():     # 使用python定义了一个名为total_posts的模板标签
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')  # 指定模板必须被latest_posts.html返回的值渲染
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]  # 这是一个字典变量
    return{'latest_posts':latest_posts}  # 返回一个字典值


@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):  # 为了避免函数名与模板名冲突，将函数名命名为markdown_format
    return mark_safe(markdown.markdown(text))

