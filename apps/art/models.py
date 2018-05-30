from django.db import models
from django.utils import timezone


# create_date = models.DateTimeField(auto_now_add=True)
# update_date = models.DateTimeField(auto_now=True)


class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cls_id = models.ForeignKey(Class)

    def __str__(self):
        return self.name


# 文章标签类
class Tag(models.Model):
    t_name = models.CharField(max_length=255, verbose_name="标签名")
    t_info = models.CharField(max_length=300, verbose_name="标签描述")
    t_createtime = models.DateTimeField(default=timezone.now(), db_index=True)

    class Meta:
        db_table = "tag"
        verbose_name = "标签"

    def __unicode__(self):
        return self.t_name


# 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255, verbose_name="标题")
    a_info = models.CharField(max_length=300, verbose_name="简介")
    a_content = models.TextField(verbose_name="内容")
    a_img = models.ImageField(null=True, blank=True, upload_to="uploads", verbose_name="图片")
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True)
    a_updatetime = models.DateTimeField(default=timezone.now)
    a_tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.a_title

    class Meta:
        db_table = "art"
        ordering = ['-a_addtime']
