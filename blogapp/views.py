#from re import L
import re
from django.shortcuts import render, redirect, get_object_or_404
#from pkg_resources import require
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.
def home(request):
    #블로그 글들을 모두 띄우는 코드
    posts = Blog.objects.all() #블로그 객체들이 모두 데이터베이스로부터 가져와짐.
    Blog.objects.filter().order_by('date') #날짜를 오름차순으로 정렬하여 필터링한다. (내림차순은 -date)
    return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수 => html 을 보여줄 필요 없음
def create(request): #new의 post 요청에 의해 create 함수가 실행된다. (urls => view.new => create)
    if(request.method=='POST'):
        post = Blog()
        post.title = request.POST['title'] #POST요청으로 들어온 request안에 있는 title을 post 객체의 title에 담아준다
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save() # model객체.save() => 모델 객체를 데이터베이스에 저장할 수 있다.
    return redirect('home') #함수가 정상적으로 실행되었다면 home으로 돌아간다.

#Django form을 이용해서 입력값을 받는 함수
#GET 요청과 (=입력값을 받을 수 있는 HTML을 갖다 줘야 함)
#POST 요청(= 입력한 내용을 데이터베이스에 저장. FORM에서 입력한 내용을 처리)
#둘 다 처리가 가능한 함수
def formcreate(request):
    if request.method == 'POST': # 새 글 생성하기 버튼을 누르면 실행되는 코드
        form = BlogForm(request.POST)
        if form.is_valid():
            #DB에 저장하는 코드
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
        # 입력 내용을 DB에 저장
    else: # GET
        # 입력 받을 수 있는 html을 가져다 주기(여기선 form_create.html)
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST': # 새 글 생성하기 버튼을 누르면 실행되는 코드
        form = BlogModelForm(request.POST)
        if form.is_valid():
            #DB에 저장하는 코드
            form.save() #form 자체가 save() 메소드를 가지고 있음
            return redirect('home')
    else: # GET
        # 입력 받을 수 있는 html을 가져다 주기(여기선 form_create.html)
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id): #인자2개 확인!
    #blog_id 번째 블로그 글을 database로 부터 가져와서
    blog_detail = get_object_or_404(Blog, pk = blog_id) #blog 객체를 가져오되,pk 값이 blog_id인 객체를 가져오기
    #blog_id 번째 블로그 글을 detail.html로 띄우는 코드
    return render(request, 'detail.html', {'blog_detail': blog_detail})