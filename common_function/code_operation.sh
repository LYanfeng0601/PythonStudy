#! /bin/bash

function git_clone()
{
    url=$1
    dest=$2
    branch=$3
    
    if [ $branch == '' ] 
    then
        branch='master'
        
    fi
    cd $dest
    expect -c "
        set timeout -1
        spawn git clone $url
        expect {
            "*yes*"{
                send "yes\r"
            }

        }
    
    
    
    "
    
}

git_clone git@github.com:LYanfeng0601/PythonStudy.git /home

