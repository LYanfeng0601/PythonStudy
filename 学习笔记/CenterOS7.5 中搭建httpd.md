## CenterOS7.5 中搭建httpd



### 一、安装httpd服务

```shell
yum install httpd
```

### 二、如果Firewalld正在运行，请允许HTTP服务。，HTTP使用80 / TCP

```shell
firewall-cmd --add-service=http --permanent
```

```shell
firewall-cmd --reload
```

### 三、修改配置文件

```shell
<Directory />
    AllowOverride none
    Require all granted  ###设置权限
</Directory>
DocumentRoot "/srv/www/htdocs"  ###设置路径
<Directory "/srv/www">
    AllowOverride None
    # Allow open access:
    Require all granted
</Directory>
<Directory "/var/www/html">
```

### 四、httpd服务器开启目录

```shell
<LocationMatch "^/+$">
    Options +Indexes   ## 此处-号变为+号
    ErrorDocument 403 /.noindex.html
</LocationMatch>

<Directory /usr/share/httpd/noindex>
    AllowOverride None
    Require all granted
</Directory>
```

### 五、启动httpd服务

```shell
systemctl start httpd
```

### 六、浏览器中测试

