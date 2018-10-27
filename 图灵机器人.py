#!C:\Users\PC\AppData\Local\Programs\Python\Python36-32\python.exe
# See http://cens.ioc.ee/projects/f2py2e/
from time import sleep
from socket import setdefaulttimeout
from re import sub
from urllib import request
from json import dumps
import speech

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
inputStr=input("输入第一句话：")
times=0
lastOUT=""
while 1:
	sleep(0.5)
	times=times+1
	if times==1 :
		text = inputStr
	else:
		text = lastOUT
	backdio=sendMessage(text)
	if times//2 == times/2 :
		print("【机器人2】"+str(times)+" ："+backdio)
		speech.say(backdio)
	else :
		print("【机器人1】"+str(times)+" ："+backdio)
		speech.say(backdio)
	lastOUT = backdio
	#inp=input("输入：")
	#backdio=sendMessage(inp)
	#print("图灵机器人：",backdio)