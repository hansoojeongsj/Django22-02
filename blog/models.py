from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)

    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    #대문자 Y는 2022인 네 글자를 표현, 소문자 m,d는 앞에꺼 빼고 뒤에 두 글자
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

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