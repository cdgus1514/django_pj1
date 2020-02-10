from django.db import models
from django.urls import reverse

# Create your models here.


# 글의 분류(일상, 유머, 정보)
class Category(models.Model):
    name = models.CharField(
        max_length=50, help_text="블로그 글의 분류를 입력하세요. (ex:일상)")

    def __str__(self):
        return self.name


# 블로그 글(제목, 작성일, 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)

    # 하나의 글을 여러가지 분류로 설정할 수 있기 떄문에 설정
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def is_content_more300(self):
        return len(self.content) > 300

    def get_content_under300(self):
        return self.content[:300]
