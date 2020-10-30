from django.conf import settings
from django.views import generic
from blog.models import Article, Tag, Category, Keyword


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGINATE_BY', 8)
    paginate_orphans = getattr(settings, 'BASE_PAGINATE_ORPHANS', 12)

