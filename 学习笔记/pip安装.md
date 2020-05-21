## 利用阿里pip源安装包
### pip  install 包名 -i https://mirrors.aliyun.com/pypi/simple/

## 安装pip命令
```shell script
yum -y install epel-release
yum -y install python-pip
```

## centos中设置pip源
### 创建~/.pip/pip.conf文件
### 配置文件
```shell script
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```