import requests
## 利用session获取cokkie
session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email": "15686270601", "password": "151932"}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"}
session.post(post_url, data=post_data, headers=headers)
r = session.get("http://www.renren.com/972854595/profile", headers=headers)
with open("rere.html", "w", encoding='utf-8') as f:
    f.write(r.content.decode())
