from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo,AreaInfo
from datetime import date
# Create your views here.
def index(request):
    context = {'title':'图书列表','list':range(10)}
    return render(request,'booktest/index.html',context)

def show_books(request):
    # 1. 查找图书表中的数据
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html',{'books':books})

def detail(request,bid):
    """c查询图书关联英雄的信息"""
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    # 使用模板展示信息
    return render(request, 'booktest/detail.html', {'book':book,'heros':heros})
def index(request):
    #1. 查询所有图书的信息
    books = BookInfo.objects.all()
    #2. 使用模板
    return render(request,'booktest/index.html',{'title':"图书信息",'books':books})
def create(request):
    #1. 新增一本图书
    b = BookInfo()
    b.btitle = '流行蝴蝶剑'
    b.bpub_date = date(1992,10,11)
    b.save()
    #2. 返回内容;重定向到index页面
    #return HttpResponse('OK')
    return redirect('/index')
def delete(request,bid):
    b = BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index')
def areas(request):
    #获取广东的上级市区；以及下级市区
    area = AreaInfo.objects.get(atitle="广州市")
    # 查询广州市的上级地区
    parent= area.aparent
    # 查询广州市的下级地区
    child = area.areainfo_set.all()
    return render(request,'booktest/areainfo.html',{'area':area,'parent':parent,'child':child})
    #return  HttpResponse("hello")

def ajax_test(request):
    return render(request, 'booktest/test_ajax.html')
def ajax_handle(request):
    return JsonResponse({'res':1})
def login(request):
    return render(request, 'booktest/login.html')
def login_check(request):
    print("helsdfgso")
    if request.is_ajax():
        all_date = request.POST
        users = request.POST.get("username")
        print(all_date)
        print(users)
        print("ajax")
    username = request.POST.get('username') // 'username'
    print(username)
    print("afdsfda")







