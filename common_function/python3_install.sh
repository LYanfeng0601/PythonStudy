#!/bin/bash
echo ${PYTHON_URL}
export ${PYTHON_VERSION}
export work_dir=/usr1/ci_work
mkdir -p ${work_dir}
cd ${work_dir}
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
rm -rf Python-3*
wget ${PYTHON_URL}/${PYTHON_VERSION}
if [ "$?"=="0" ];then
	echo "wget success"
else
	echo "wget fail"
	exit 1
fi
tar xf ${PYTHON_VERSION}
cd Python-3*
./configure prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python
python --version
