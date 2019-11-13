import requests


class TieBaSpide(object):
    """docstring for TieBaSpide"""

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_tmp = "https://tieba.baidu.com/f?ie=utf-8&kw=" + tieba_name + "&pn={}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    def get_url_list(self):  # 构建rul列表
        url_list = []
        for i in range(1000):
            url_list.append(self.url_tmp.format(i * 50))
        return url_list

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "C:/Users/liyanfeng/Desktop/results/{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w",encoding="utf-8") as f:
            f.write(html_str)

    def run(self):  # 主要实现逻辑
        # 1 构建俩url列表
        url_list = self.get_url_list()
        # print(url_list)
        # 2 遍历 发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)  # 保存

if __name__ == '__main__':

    tieba_spider = TieBaSpide("中国")
    tieba_spider.run()
