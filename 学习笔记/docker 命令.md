## docker 命令

### 1. docker的帮助命令

```shell
docker version  ##  查询docker的版本号
docker info		## 显示docker的详细信息
docker --help   ## docker的帮助命令
```

### 2. docker的镜像命令

- images

```shell
docker images  ## 列举本地可以运行的镜像
docker images -q ## 只显示镜像id
docker images -a  ## 列举所有的惊醒，包括分层的
docker images -qa ## 显示所有的镜像的id
docker images --digests  ## 显示摘要信息
docker images --digests --no-trunc ## 不截取摘要信息，全部显示
```

- search

```shell
docker search tomcat  # 查询镜像库中的镜像
docker search -s 30 tomcat ## 只查询星数超过30的镜像
```

- pull

```shell
docker pull tomcat   ## 默认获取tomcat最新版
```

- rmi

```
docker rmi -f hello-world ## -f 强制删除
docekr rmi  ID ## 删除镜像id;
docker rmi -f $(docker images -qa)  ## 删除所有的镜像
```

### 3.容器的相关命令

```shell
docker run -it centos## 新建并启动容器; -i: 交互式操作;-t: 终端；-d 后台运行（返回id值）
docker ps ##   列出所有在运行得容器
docker run -it  --name centeosss centos  ##--name给容器起个别名
docker ps -a ## 列出正在运行的和未运行的容器
docker ps -l ##   上次运行的容器
docker ps -n 3  ## 显示最近三次运行的容器
ctrl + p + q ## 只是退出容器的终端。但是容器还在运行
docker start id # 启动容器
docker restart id  #重启容器
docekr stop id # 停止容器
docker kill id  ## 强制关闭容器
docker rm id #  删除容器
docker rm -rf $(docker ps -a -q) ## 删除所有的容器
docker ps -a -q | xargs docker rm ## 删除所有的容器
docker logs -t -f --tail id #查询具体容器的的日志
docker top 容器id  ## ##查看容器的
docker run -d 0f3e07c0138f /bin/sh -c "while true;do;echo 'hello';sleep 2;done" ##后台运行，不会推出
docker inspect 容器id  ##查询当前正在运行的容器的结构（细节）；以json形式返回
ctrl + p +q ##推出容器，不会停止容器；exit退出停止容器
docker exec -t b13a616c17d9 ls -l /tmp  ## 直接在容器中查询ls，实际不会进入容器
docker attach b13a616c17d9 == docker exec -it b13a616c17d9 /bin/bash ##直接进入容器
##从容器拷贝文件到主机上
docker cp 容器id:容器内路径 目的主机路径

```

### 4.docker容器数	据卷

- 容器的持久化
- 容器间的共享+宿主机跟容器间的共享
- 容器内的添加：直接命令添加；DockerFile 添加
- 命令添加

```
docker run -it -v /home/mydata:/home/test 0f3e07c0138f # 将宿主机路径/home/mydata跟容器 /home/test  数据共享 容器关闭 数据任然共享
docker run -it -v /home/mydata:/home/test：ro 0f3e07c0138f #以只读方式；共享，只允许主机单线修改数据，容器没法修改
```

- DockerFile 添加

  ​

  ​

  ​

  ​

  ​

  ​

  ​

  ​