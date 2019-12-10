## docker（二）

### 1. docker 容器间的数据共享

```shell
docker run -it --name doc1 -v /home/doc1:/home/doc1 0f3e07c0138f  ## 创建doc1 并创建数据卷
docker run -it --name doc2 --voluems-from doc1 0f3e07c0138f  ## 创建doc2 并继承doc1
docker run -it --name doc3 --volumes-from doc1 0f3e07c0138f ## 创建doc3 并继承doc1
doc1 doc2 doc3 /home/doc1 下的数据会共享
注意：容器间的信息传递，数据卷的生命周期一直到持续到没有数据传递
```

### 2. DockerFile

- 编写流程：编写dockerfile---》执行docker  build-

- 定义：Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。

- dockerfile内容基础知识

  1. 每条指令为大写字母，并后面至少跟一个参数
  2. 指令按照从上到下，顺序执行
  3.  “#” 表示注释
  4. 每条指令都会创建一个新的镜像层，并对镜像进行提交

- dockerfile的执行过程

  1. docker从基础镜像运行一个容器
  2. 执行一条指令并对容器进行修改
  3. 执行类似commit的操作提交一个新的镜像
  4. docker再基于刚提交的镜像运行一个容器
  5. 执行dockerfile中的下一条指令直到所有执行执行完成

- dockerfile的体系结构

  1. FROM；基础镜像，当前镜像是基于那个镜像的

  2. MAINTAINER;镜像维护者的姓名和邮箱

  3. RUN；容器构建时候需要运行的命令

  4. EXPOSE；当前容器对外暴漏的端口

  5. WORKDIR；指定创建容器后，终端默认登陆的进来工作目录，一个落脚点

  6. ENV；设置环境变量

  7. ADD；拷贝+解压缩+处理rul

  8. COPY；拷贝

  9. VOLUME；容器数据卷，保存数据和持久化

  10. CMD；指定容器启动时运行的命令，可以多个命令，但是只有最后个生效

  11. ENTRYPOINT；指定容器启动时运行的命令，可以多个命令

  12. ONBUILD；触发器；当构建一个被继承的DockerFile时运行命令，父镜像在被子镜像继承后父镜像的onbulid会触发

  13. USER；设置组跟用户

      ​