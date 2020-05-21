import requests
#session = requests.session()
#post_url = "http://www.renren.com/SysHome.do"
#post_data = {"email": "15686270601", "password": "151932"}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36",
    "Cookie": "anonymid=k2xaig6eybrbkw; depovince=SXI; _r01_=1; JSESSIONID=abcDjJ5S9m8urhX-61K5w; ick_login=f6847493-7cbb-412d-ba66-92ee3861b3fa; ick=3b8182e8-6521-4540-b981-43e298ac0c39; XNESSESSIONID=9b617c15dd32; jebe_key=1170d07a-13b8-49c8-a195-3fc8b1846d5d%7C5c9a9c2b6fe18f0584a9cf96d60671d4%7C1573650068996%7C1%7C1573650073869; jebe_key=1170d07a-13b8-49c8-a195-3fc8b1846d5d%7C5c9a9c2b6fe18f0584a9cf96d60671d4%7C1573650068996%7C1%7C1573650073872; wp_fold=0; wp=0; first_login_flag=1; ln_uact=15686270601; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=d39c8e23-ba40-43fe-93f7-c4af9f8f85cf|||||; _de=1ECADF9B50D31E2603402C98A48C1D9D; p=2c43f9bfd55da1dba94ecfb5e6caa44a5; t=98cb9389eee5faaeaec42f641d9b01385; societyguester=98cb9389eee5faaeaec42f641d9b01385; id=972854595; xnsid=9b136b1d; ver=7.0; loginfrom=null"}
#session.post(post_url, data=post_data, headers=headers)
r = requests.get("http://www.renren.com/972854595/profile", headers=headers)
with open("rere2.html", "w", encoding='utf-8') as f:
    f.write(r.content.decode())
