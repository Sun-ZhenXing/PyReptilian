import socket
import urllib.request
import urllib.parse
import re

def getRandomPage():
	# 当小豆无话可说时执行
	URLmain="http://api.douqq.com/?key=MlVZZjR3N0ZqVj1ISXBZTG1RVDBMMEI9VEJjQUFBPT0&msg=%E4%B8%80%E8%A8%80"
	timeout = 5
	socket.setdefaulttimeout(timeout)
	req = urllib.request.Request(URLmain)
	a = urllib.request.urlopen(req).read()
	out_str=str(a,encoding="utf-8")
	return out_str

while True:
	try:
		main_str=input("主人：")
		word=urllib.parse.quote(main_str)
		url_api="http://api.douqq.com/?key=MlVZZjR3N0ZqVj1ISXBZTG1RVDBMMEI9VEJjQUFBPT0&msg="+word
		timeout = 5
		print(url_api)
		socket.setdefaulttimeout(timeout)
		req = urllib.request.Request(url_api)
		a = urllib.request.urlopen(req).read()
		if(a==b""):
			# 页面不存在
			out_str=getRandomPage()
		else:
			out_str=str(a,encoding="utf-8")
	except:
		print("#####超时错误！#####")
		out_str= getRandomPage()
	print("小豆机器人："+out_str+"\n")
