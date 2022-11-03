#View: HTTP요청을 수신하고 HTTP응답을 반환하는 요청처리함수
#Model을 통해 요청을 충족시키는데 필요한 데이터에 접근하고 Template에게 응답의 서식설정을 맡김
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

    # 템플릿 모델명_list.html : post_list.html
    # 파라미터 모델명_list : post_list

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {
        'category' : category,    #템플릿에 넘겨줄 값 딕셔너리 형태로
        'post_list' : post_list,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count
    })

    # 템플릿 모델명_detail.html : post_detail.html
    # 파라미터 모델명 : post

#def index(request):
#    posts1 = Post.objects.all().order_by('-pk') #pk역순으로 나열
#    return render(request, 'blog/index.html', {'posts':posts1}) #urls.py와views.py와템플릿파일로블로그index페이지만들기 3

#def single_post_page(request, pk):
#    post2 = Post.objects.get(pk=pk)
#    return render(request, 'blog/single_post_page.html', {'post':post2})