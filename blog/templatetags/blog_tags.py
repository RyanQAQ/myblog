from django import template
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
