import socket
import urllib.request
import urllib.parse
import re
import json

def check_back_str(backStr):
	bool1=re.search("你输入的内容真的好深奥呀",backStr)
	bool2=re.search("看不懂",backStr)
	bool3=re.search("我实在听不懂你在说什么",backStr)
	bool4=re.search("听不懂",backStr)
	bool5=re.search("我不明白",backStr)
	bool6=re.search("我都无法理解",backStr)
	bool7=re.search("理解能力有限",backStr)
	bool8=re.search("读不懂你的话",backStr)
	bool9=re.search("就不能来点简单点",backStr)
	bool10=re.search("没听明白",backStr)
	bool11=re.search("听的我一头雾水",backStr)
	bool12=re.search("你到底在说什么呢",backStr)
	bool13=re.search("你到底在说什么呢",backStr)
	if(bool1 or bool2 or bool3 or bool4 or bool5 or bool6 or bool7 or bool8 or bool9 or bool10 or bool11 or bool12 or bool13):
		print("##########小i没听明白！##########")

def format_func(str_xiaoi):
	str_xiaoi=re.sub("\\\\","",str_xiaoi)
	str_xiaoi=re.sub("[\s\S]*__webrobot_processMsg","msg",str_xiaoi)
	str_xiaoi=re.sub('[\s\S]*\"body\":\{',"msg({",str_xiaoi)
	str_xiaoi=re.sub('[\s\S]*content\":\"',"",str_xiaoi)
	str_xiaoi=str_xiaoi[:-22]
	if re.search(r"\[.+\]",str_xiaoi):
		# 检测到网址
		str_xiaoi=re.sub(r"\[.+http","http",str_xiaoi)
		str_xiaoi=re.sub(r'.]',"",str_xiaoi)
		str_xiaoi=re.sub(r'\[/lin',"",str_xiaoi)
	if re.search("rn",str_xiaoi):
		# 检测到换行符
		str_xiaoi=re.sub("rn","",str_xiaoi)
	if re.search(r"u[0-9abcdef]{4}",str_xiaoi):
		# 检测到HTML编码
		str_xiaoi=re.sub(r"u[0-9abcdef]{4}","",str_xiaoi)
	return str_xiaoi

# http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%2296e80737a4ec461aacfa3de49ae673ea%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%22b345ff113b6f45229e1cb2f231561866%22%2C%22body%22%3A%7B%22content%22%3A%22%E4%BD%A0%E5%A5%BD%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1552199072937
# 原来的URL已经过期，新的URL提供测试

while True:
	try :
		inputStr = input("我：")
		word=urllib.parse.quote(inputStr)
		# 更新网址：
		url_api="http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%2296e80737a4ec461aacfa3de49ae673ea%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%22b345ff113b6f45229e1cb2f231561866%22%2C%22body%22%3A%7B%22content%22%3A%22%E4%BD%A0%E5%A5%BD%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1552199072937"
		# E4%BD%A0%E5%A5%BD
		url_new=re.sub("E4%BD%A0%E5%A5%BD",word,url_api)
		timeout=7
		socket.setdefaulttimeout(timeout)
		req = urllib.request.Request(url_new)
		a = urllib.request.urlopen(req).read()
		main_out_str=str(a,encoding="utf-8")
		main_out_str=format_func(main_out_str)
		print(main_out_str)
		check_back_str(main_out_str)
	except:
		print("##########超时错误##########")
