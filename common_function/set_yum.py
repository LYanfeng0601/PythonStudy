#!/bin/bash

echo "*********************start set yum*************************"
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
sed -i  's/$releasever/7/g' /etc/yum.repos.d/CentOS-Base.repo
yum clean all
yum list


