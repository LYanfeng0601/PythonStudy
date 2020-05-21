## docker中部署mysql

### 一，拉取镜像

```shell
docker pull docker.io/mysql
```

### 二、运行镜像，创建容器

```shell
docker run  -p 12345:3306 --name mysql -v /home/mysql/conf:/etc/mysql/conf.d -v /home/mysql/log:/logs -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d d435eee2caa5
docker exec -it 192f3ae5b180 /bin/bash  #进入容器
mysql -uroot -p  ## 进入数据库

```

三、备份数据库

```mysql
mysqldump -uroot -p --all-databases > sqlfile.sql
```

