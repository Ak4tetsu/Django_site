from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','در انتظار'),
        ('published','انتشار یافته'),
    )
    title = models.CharField(max_length=60, verbose_name= "عنوان")
    slug = models.SlugField(max_length=100, verbose_name="عنوان پیوسته")
    body = models.TextField(verbose_name="متن کامل")
    publish = models.DateTimeField(default= timezone.now, verbose_name="انتشار")
    created = models.DateTimeField(auto_now_add= True, verbose_name="ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="ویرایش")
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default= 'draft', verbose_name="وضعیت")

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = "پست ها"



    def __str__(self) -> str:
        return f'Post object(id = {self.id}, title = {self.title})'