import configparser


class configParse(object):
    """docstring for ClassName"""

    def __init__(self, file_path, section):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.file_path)
        self.section = section

    def get_value(self,key,selctions=None):
    	if selctions == None:
    		selctions = self.section
    	return self.config.get(selctions, key)
if __name__ == '__main__':

	##创建对象时，需要指定conf文件的路径以及操作的section名称
    test2 = configParse("E:/PythonStudy/conf/common_conf", "docker_mysql")
    ## 通过get_value方法获取key对应的vaule值：此处可以只指定key值；也可以指定key值及section名称[key,section]
    print(test2.get_value("host"))
    print(test2.get_value("host","docker_mysql")) #[key]
    print(test2.get_value("a","test1")) #[key,section]

