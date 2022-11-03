from django.contrib import admin #Post 모델 admin에 등록하기
from .models import Post, Category, Tag#Post 모델 admin에 등록하기, Category 모델 admin에 등록하기

# Register your models here.
admin.site.register(Post) #Post 모델 admin에 등록하기

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Tag, TagAdmin)

#SlugField자동으로생성하는admin기능만들기 (밑에 세줄과 위 두번째 Category)
# prepopulated_fields
# name필드값으로slug를자동생성하도록설정