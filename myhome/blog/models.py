from django.db import models
from django.contrib import admin
# Create your models here.
#创建数据库表
class BlogsPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)

