## docker中部署Jenkins

###  一、安装docker

### 二、创建docker的容器的工作目录

```shell
mkdir /home/jenkins；chown -R 1000:1000 /home/jenkins
```

 ### 三、查询jenkins的镜像-=--

```shell
docker search jenkins
```

### 四、获取容器镜像

```shell
docker pull docker.io/jenkins
```

### 五、启动容器

```shell
docker run -itd -p 9090:8080 -p 50000:50000 --name jenkins --privileged=true  -v /home/jenkins:/var/jenkins_home jenkins:latest
```

##  六、访问地址

- <http://192.168.0.103:9090/jenkins>

  七、服务器重启后的启动方式

###  七、服务器重启后的启动方式

```shell
docker start jenkins
```

