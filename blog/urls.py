#URLs: 요청URL을 기준으로 HTTP요청을 적절한뷰(view)로 보내주기 위해 사용
from django.urls import path
from . import views

urlpatterns=[  # IP주소/blog/
    path('', views.PostList.as_view()), #urls.py와 views.py와 템플릿파일로 블로그index페이지만들기2
                                        #ListView로 포스트목록페이지 만들기
    path('<int:pk>/', views.PostDetail.as_view()),  #DetailView로포스트상세페이지만들기
    path('<int:pk>/new_comment/', views.new_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('category/<str:slug>/', views.category_page), #IP주소/blog/category/slug/

    path('tag/<str:slug>/', views.tag_page) #IP주소/blog/tag/slug/

    #path('', views.index), # IP주소/blog
    #path('<int:pk>/', views.single_post_page)
]
        #ListView는(모델명)_list.html을템플릿으로인지  index.html을post_list.html로변경
        #DetailView는(모델명)_detail.html을템플릿으로인지  single_post_page.html을post_detail.html로변경