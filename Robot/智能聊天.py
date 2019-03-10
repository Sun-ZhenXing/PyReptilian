# 图灵已经限制次数了
# 使用我刚更新的机器人
from time import sleep
from socket import setdefaulttimeout
from re import sub
from urllib import request
from json import dumps
from speech import say
import AudioTest # 自定义模块

# 接口地址 http://openapi.tuling123.com/openapi/api/v2
print("[INFO] 模块加载完成")
def sendMessage(text):
	data0={
		"reqType":"0",
		"perception": {
			"inputText": {
				"text": "附近的酒店"
			},
			"selfInfo": {
				"location": {
					"city": "北京",
					"province": "北京",
					"street": "信息路"
				}
			}
		},
		"userInfo": {
			"apiKey": "038aed41be7b451daac8d74340b9e0fd",
			"userId": "316470"
		}
	}
	data0["perception"]["inputText"]["text"]=text
	url_api="http://openapi.tuling123.com/openapi/api/v2"
	timeout = 5
	setdefaulttimeout(timeout)
	req = request.Request(url_api,data=dumps(data0).encode("utf-8"))
	req.add_header('Content-Type','application/json')
	response=request.urlopen(req)
	outjson=str(response.read(),encoding="utf-8")
	# print("[INFO] 服务器数据\n",outjson+"\n[/INFO]")
	out_str=sub(r".+value","",outjson)
	out_str=sub(r'"}}]}',"",out_str)
	out_str=out_str[12:] 
	return out_str

while 1:
	try:
		inp=AudioTest.MainMethod(10)['result'][0]
		print('主人：',inp)
		backdio=sendMessage(inp)
		print("图灵机器人：",backdio)
		say(backdio)
	except:
		try:
			backdio=sendMessage(" ")
			print("图灵机器人：",backdio)
			say(backdio)
		except:
			print("请求出错！！")
