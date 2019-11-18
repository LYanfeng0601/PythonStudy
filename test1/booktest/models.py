from django.db import models

# Create your models here.
class BookInfoManage(models.Manager):
    #改变查询的结果集
    def all(self):
        # d调用父类的all方法
        books = super().all() #QuerySET
        books = books.filter(isDelete=False)
        return books
        # 封装函数，操作模型类的数据表
    def create_book(self, title, pub_date):
            # 创建模型类对象self.model可以获得模型类
        book = self.model() #获取self所在的模型类
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        # 将数据插入进数据表
        book.save()
        return book



class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除
    objects = BookInfoManage()
    #book = models.Manager()
    # 定义元选项
    class Meta:
        db_table = 'bookinfo' #指定表名
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中
'''
class NewsType(models.Model):
    type_name = models.CharField(max_length=20)
class NewsInfo(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    news_type = models.ManyToManyField('type_name')  #多对多的关系

class EmployeeBasicInfo(models.Model):
    name =  models.CharField(max_length="10")
    genter = models.BooleanField(default=False)
    age = models.IntegerField()
class EmployeeDetailInfo(models.Model):
    addr = models.CharField(max_length='200')
    employee_basic = models.OneToOneField('EmployeeBasicInfo')  #一对一
'''
class AreaInfo(models.Model):#地区模型类
    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self',null=True,blank=True)