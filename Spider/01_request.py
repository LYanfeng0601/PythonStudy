import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def main():
    heades = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    params = {'wd':"传智播客"}
    response = requests.get("http://www.baidu.com/s?",headers=heades,params=params)  #发送带heander的请求
    print(heades)
    code_status = response.status_code
    print(response.content.decode('utf-8'))
    print(response.request.url)
if __name__ == '__main__':
    main()
