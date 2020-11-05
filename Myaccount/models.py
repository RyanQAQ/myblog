from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True, null=True, verbose_name='昵称')
    link = models.URLField('', blank=True, help_text='提示：网址必须填写以http开头的完整形式')
    avatar = ProcessedImageField(upload_to='avatar', default='avatar/default.png',verbose_name='头像',
                                 processors=[ResizeToFill(100,100)],format='JPEG',options={'quality':95})

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if len(self.avatar.name.split('/')) == 1:
            self.avatar.name = self.username + '/' + self.avatar.name
        super(User, self).save()

