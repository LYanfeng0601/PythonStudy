#!/bin/bash

function usage()
{
    echo "Usage:sh sshcmd.sh -c "command" -m "machine_ip" -u "loginuser" -p "loginpwd""
}

function delete_know_hosts()
{
    know_hosts=/root/.ssh
    know_hosts>${know_hosts}
}

function sshcmd_common()
{
    local cmd=$1
    local testip=$2
    local pwd=$3
    local user=$4
    [ -z "$testip" -o -z "$pwd" -o -z "$cmd" -o -z $user ] && return 1
    expect << EOF
    set timoout -1
    proc remote_exec {testip pwd cmd} { #定义函数
        spawn ssh root@\${testip}
        exp_internal 0  ## exp_internal用来打开调试模式1表示打开；0表示关闭
        expect {
            "yes/no" { send "yes\\r";exp_continue} #exp_continue 表示当问题不存在时回答下一个问题
            "*password:" {send "\$pwd\\r"}
        } 
        expect "*#"
        send "\$cmd\\r"
        expect "*#"
        send "exit"
        close
    }
 
    remote_exec "$testip" "$pwd" "$cmd"
EOF
   
}
##mian##
while getopts "c:m:p:u:h" OPTIONS
do 
    case $OPTIONS in
        c) execcmd=$OPTARG
        ;;
        m) machine_ip=$OPTARG
        ;;
        u) loginuser=$OPTARG
        ;;
        p) loginpasswd=$OPTARG
        ;;
        h) usage
        ;;
        \?) ehco "ERROR INVALID parameter";usage;exit 1
        ;;
        *) ehco "ERROR INVALID parameter";usage;exit 1 
        ;;
    esac
done

if [ "$machine_ip" == '' -o "$execcmd" == '' -o "$loginuser" == '' -o "$loginpasswd" == '' ];
then
    echo "please give right paramters"
    usage
    exit 1 
fi
# delete_know_hosts
cat /dev/null >/root/.ssh/know_hosts
sshcmd_common "$execcmd"  "$machine_ip" "$loginuser" "$loginpasswd" 