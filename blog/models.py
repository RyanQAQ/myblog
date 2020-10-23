from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import markdown


class Keyword(models.Model):
    """关键词模型"""
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'keyword'
        verbose_name = '关键词'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签模型"""
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=240, help_text='用来作为SEO的description')

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('blog:tag', kwargs={'slug': self.slug})
        pass

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        # return Article.objects.filter(tags=self)
        pass


class Category(models.Model):
    """文章分类模型"""
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=240, help_text='用来作为SEO的description')

    class Meta:
        db_table = 'category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('blog:category', kwargs={'slug': self.slug})
        pass

    def get_article_list(self):
        # return Article.objects.filter(category=self)
        pass


class Article(models.Model):
    """文章模型"""
    title = models.CharField(max_length=150, verbose_name='文章标题')
    author = models.CharField(max_length=50, verbose_name='作者')
    summary = models.TextField(max_length=230, verbose_name='文章摘要')
    body = models.TextField(verbose_name='文章内容')
    image = models.ImageField(upload_to='image', default='https://tendcode.com/cdn/blog/20200723/pypi.png')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    keywords = models.ManyToManyField(Keyword, verbose_name='文章关键词',
                                      help_text='文章关键词，用来作为SEO中的keywords，一般3-4个足够')

    class Meta:
        db_table = 'articles'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('blog:detail', kwargs={'slug': self.slug})
        pass

    def body_to_markdown(self):
        # return markdown.markdown(self.body, extensions=[
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',
        # ])
        pass

    def update_view(self):
        # self.views += 1
        # self.save(update_fields=['views'])
        pass

    def get_pre(self):
        # return Article.objects.filter(id__lt=self.id).order_by('-id').first()
        pass

    def get_next(self):
        # return Article.objects.filter(id__gt=self.id).order_by('id').first()
        pass