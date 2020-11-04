from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views import generic
from blog.models import Article, Tag, Category, Keyword

from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGINATE_BY', 8)
    paginate_orphans = getattr(settings, 'BASE_PAGINATE_ORPHANS', 2)


class DetailView(generic.DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article'


class CategoryView(generic.ListView):
    model = Article
    template_name = 'category.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', 8)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 2)

    def get_queryset(self, **kwargs):
        queryset = super(CategoryView, self).get_queryset()
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return queryset.filter(category=cate)


class TagView(generic.ListView):
    model = Article
    template_name = 'tag.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', 8)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 2)

    def get_queryset(self, **kwargs):
        queryset = super(TagView, self).get_queryset()
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return queryset.filter(tags=tag)


class ArchiveView(generic.ListView):
    model = Article
    template_name = 'archive.html'
    context_object_name = 'articles'
    paginate_by = 200
    paginate_orphans = 50


class MySearchView(SearchView):
    context_object_name = 'search_list'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', 8)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 2)
    queryset = SearchQuerySet().order_by('-views')

