import re
from django import template
from django.utils.safestring import mark_safe
from ..models import Article, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_tag_list():
    """获取标签列表"""
    return Tag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)


@register.simple_tag
def get_category_list():
    """获取分类列表"""
    return Category.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)


@register.simple_tag
def get_article_count():
    """获取文章总数"""
    return Article.objects.count()


@register.simple_tag
def title_highlight(text, q):
    '''自定义标题搜索词高亮函数，忽略大小写'''
    if len(q) > 1:
        try:
            text = re.sub(q, lambda a: '<span class="highlighted">{}</span>'.format(a.group()),
                          text, flags=re.IGNORECASE)
            text = mark_safe(text)
        except:
            pass
    return text
