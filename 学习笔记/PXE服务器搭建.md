## PXE服务器搭建

### 一、安装配置安装DHCP

```shell
[root@PXE ~]# yum install dhcp   # 安装dhcp server

[root@PXE ~]# rpm -ql dhcp
/etc/dhcp
/etc/dhcp/dhcpd.conf   # dhcpd配置文件
/etc/rc.d/init.d/dhcpd   # dhcpd启动文件
/usr/sbin/dhcpd   # 启动脚本配置文件
[root@PXE pxelinux.cfg]# vi /etc/dhcp/dhcpd.conf   # 调整配置文件
option domain-name "itwish.cn";
option domain-name-servers 192.168.0.103 ;

default-lease-time 600;
max-lease-time 7200;

log-facility local7;

subnet 192.168.0.0 netmask 255.255.255.0 {  # 定义子网
  range 192.168.0.10 192.168.0.100;
  option routers 192.168.0.1;
  next-server 192.168.0.103;	# 注：添加 tftp服务器地址
  filename="pxelinux.0";	#注：告诉TFTP目录下的bootstarp文件
}
#注：配置文件中以";" 号结尾 ，且需添加next-server 和filename 项
```

- 启动dhcp并验证dhcpd进程是否处于监听状态

```shell
[root@PXE ~]# chkconfig --add dhcpd

[root@PXE ~]# chkconfig dhcpd on

[root@PXE ~]# service dhcpd start
Starting dhcpd:                                            [  OK  ]

[root@PXE ~]# ps aux | grep dhcpd     # 验证dhcpd 启动
dhcpd     14087  0.0  0.1  48324  3572 ?        Ss   03:13   0:00 /usr/sbin/dhcpd -user dhcpd -group dhcpd
root      14108  0.0  0.0 103272   840 pts/0    S+   03:14   0:00 grep dhcpd

[root@PXE ~]# ss -tunl | grep 67
udp    UNCONN     0      0                      *:67                    *:*

```

### 二、安装 配置TFTP服务

```shell
[root@PXE ~]# yum install xinetd tftp-server

[root@PXE ~]# rpm -ql tftp-server  
/etc/xinetd.d/tftp    # 配置文件路径
/var/lib/tftpboot    # 默认tftp存储目录

[root@PXE ~]# vi /etc/xinetd.d/tftp 
# default: off    
service tftp
{
        disable = no    # no 表明tftp处于启用状态 ，yes 表示tftp处于禁用状态
        socket_type             = dgram
        protocol                = udp
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
        server_args             = = -s /tftpboot -c # 设置tftp存储目录
        per_source              = 11
        cps                     = 100 2
        flags                   = IPv4
}
[root@PXE ~]# chkconfig xinetd on

[root@PXE ~]# chkconfig tftp on

[root@PXE ~]# service xinetd start
Starting xinetd: 

[root@PXE ~]# ss -tunl | grep 69
udp    UNCONN     0      0                      *:69                    *:*
```



