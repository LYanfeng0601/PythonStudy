import requests
# 保存图片
response = requests.get("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1962349622,1091993405&fm=26&gp=0.jpg")
with open("a.png","wb") as f: # 保存图片 “wb”
	f.write(response.content)