# docker加速器配置

## 1. 修改配置文件 

```shell
vim /etc/docker/daemon.json
{
    "registry-mirrors": ["<https://n5lhj1jl.mirror.aliyuncs.com>"]
}
systemctl daemon-reload
systemctl restart docker
```

## 2. 测试

```shell
docker run hello-world
```
