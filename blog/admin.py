from django.contrib import admin
from blog.models import Article, Tag, Category, Keyword

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Keyword)
