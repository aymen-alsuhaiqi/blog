from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField('العنوان',max_length=100)
    content = models.TextField('المحتوى')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    media = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    created_date = models.DateTimeField('تاريخ النشر',auto_now_add=True)
    updated_date = models.DateTimeField('تاريخ التحديث',auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField('التعليق')
    created_date = models.DateTimeField('تاريخ النشر',auto_now_add=True)
    updated_date = models.DateTimeField('تاريخ التحديث',auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} | {self.post.title}'
    