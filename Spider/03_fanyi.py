import requests
import json
import sys
#query_string = sys.argv[1]
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36", "cookie": "BAIDUID=E088FC29E9CE0787A0092F5F5A5C46FA:FG=1; BIDUPSID=E088FC29E9CE0787A0092F5F5A5C46FA; PSTM=1551019541; BDUSS=M1NlY2TVJhY01Md2MxaWo1aVpkcFg0MGxxckhna2ROS05NNHRXUS1Wei1uTFZjQVFBQUFBJCQAAAAAAAAAAAEAAAA70Fivt-fT6jA2MDExMDI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP4Pjlz-D45caD; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1443_21093_29568_29700_29221_26350_29999; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1572960333; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_267a757dde5271a8ac40190390498efa7bfe_300_1572960333360_222.90.13.29_fb34e310; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1572960647; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1572960647; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1572960647; yjs_js_security_passport=98e21e8f24bcb361cfbfbc6f385ab7f6ddd8d69d_1572960658_js"}
post_data = {
    "query": "人生苦短，我用python",
    "from": "zh",
    "to": "en",
	"token": "3acd8f85281cf0f7fa74e81570b94ef1",
	"sign": "650687.855694"
}
post_url = "https://fanyi.baidu.com/basetrans"
r = requests.post(post_url, data=post_data, headers=headers)
# print(r.content.decode())
dict_ret = json.loads(r.content.decode())
ret = dict_ret['trans'][0]["dst"]
print("result is :", ret)
