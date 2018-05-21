# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-8


from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPost(Feed):
    title = 'My Blog'
    link = '/blog/'
    description = 'New Post Of My Blog'

    def items(self):
        return Post.published.all()[:5]

    def item_description(self, item):
        return truncatewords(item.body, 30)  # 使用内置的模板过滤器构建帖子的描述信息