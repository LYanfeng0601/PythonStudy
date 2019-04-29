#coding=utf-8
echo ${PYTHON_URL}
export ${PYTHON_VERSION}
export work_dir=/usr1/ci_work
mkdir -p ${work_dir}
cd {work_dir}
wget ${PYTHON_URL}/${PYTHON_VERSION}
