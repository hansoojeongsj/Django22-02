#Model: 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가,수정,삭제)하고 쿼리하는 방법을 제공하는 파이썬 객체
#__str__ 함수정의: __str__함수로 모델의 string 표현 방법 정의하기 함수정의하면 post의 pk값과 title로 표현
#__str__  첫번째 게시물(1) -> [1]첫번째 게시물
#자동으로 작성 시각과 수정 시각 저장하기 밑에 주석참고
from django.db import models  #post모델만들기  makemigrations하는건가(데이터베이스에 Post모델 반영하기)
from django.contrib.auth.models import User
import os

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  #IP주소/blog/tag/slug/
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)

    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    #대문자 Y는 2022인 네 글자를 표현, 소문자 m,d는 앞에꺼 빼고 뒤에 두 글자
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    # 새로 작성 했을 때 생성: auto_now_add, 수정 했을 때 업데이트: auto_now
    #하고 마이그레이션 하기(?) python manage.py makemigrations -> migrate -> runserver
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)
    #ManyToManyField에는  null=True, on_delete=models.SET_NULL 이거 포함하고 있음

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author} : {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #[-1]:주어진 배열의 가장 마지막 원소
        #a.txt -> a txt
        #b.docx -> b docx
        #c.xlsx -> c xlsx
        #a.b.c.txt -> a b c txt [1]인 경우 b가 리턴됨. 확장자 아님.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE 유저가 지워지면 모두 다 지워지게?
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'