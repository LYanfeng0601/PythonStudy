from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
# Create your views here.
def index(request):
    context = {'title':'图书列表','list':range(10)}
    return render(request,'booktest/index.html',context)

def show_books(request):
	# 1. 查找图书表中的数据
	books = BookInfo.objects.all()
	


