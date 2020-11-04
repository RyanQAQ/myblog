from django.urls import path
from blog.views import IndexView, DetailView, CategoryView, TagView, ArchiveView, MySearchView

app_name = 'blog'

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),  # 首页
    path(r'article/<slug>/', DetailView.as_view(), name='article'),  # 文章详情页
    path(r'category/<slug>', CategoryView.as_view(), name='category'),  # 分类文章
    path(r'tag/<slug>', TagView.as_view(), name='tag'),   # 标签文章
    path(r'archive/', ArchiveView.as_view(), name='archive'), # 归档
    path(r'search/', MySearchView.as_view(), name='search')   # 全文搜索
]
