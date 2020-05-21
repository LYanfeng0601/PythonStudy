# Flask部署（nginx + gunicorn + flask）
## 一、安装gunicorn
```shell script
pip install gunicorn
```
## 二、运行命令
```shell script
gunicorn -w 4 -b 192.168.0.103:5001 -D --access-logfile ./logs/log main:app
```