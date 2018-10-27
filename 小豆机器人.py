#!C:\Users\PC\AppData\Local\Programs\Python\Python36-32\python.exe
# See http://cens.ioc.ee/projects/f2py2e/
print("##########玩命加载中！！##########")
import socket
import urllib.request
import urllib.parse
import re
out_str=" "
print("##########模块导入成功！##########")
print("# 智能小豆机器人使用帮助\n\
# 帮助 输入：帮助\n\
# 每日一句 输入：每日一句\n\
# 猜谜 输入：猜谜\n\
# 笑话 输入：笑话\n\
# 空气质量 输入：城市名+空气质量")
# ~~~~~~~~~~帮助信息~~~~~~~~~~
print("# 手机归属地 输入：手机号(例如：输入：13838383838)\n\
# 翻译 汉译英 输入：翻译+中文(例如：输入：翻译我爱你)\n\
# 百科查询 输入：什么是+名词(例如：输入：什么是机器人)\n\
# 历史上的今天 输入：历史上的今天\n\
# 百家姓 输入：李\n\
# 电影 输入：电影+电影名(机器人知道很少的电影))\n\
# 知道问答 输入：…………的原因 或 为什么…………\n\
# 脑筋急转弯 输入：脑筋急转弯")

def whenTimeOut():
	#超时错误或者页面不存在
	if((re.search("好|在|hello|Hello|Hi|hi",main_str))):
		# 友善地打招呼
		out_str="你好呀，我是小豆机器人，我在这呢 ^_^ "
	elif(re.search("再见|bye",main_str)):
		# 委婉地再见
		out_str="再见啦！下次再聊啊！"
	elif(re.search("你妈|你妹|去你|fuck|Fuck",main_str)):
		# 发现有人骂我，义不容辞拒绝
		out_str="咱们有话好好说，别动不动就…………"
	else:
		out_str=getRandomPage()
	return out_str

def getRandomPage():
	#当小豆无话可说时执行
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
		socket.setdefaulttimeout(timeout)
		req = urllib.request.Request(url_api)
		a = urllib.request.urlopen(req).read()
		if(a==b""):
			# 页面不存在
			out_str=whenTimeOut()
		else:
			out_str=str(a,encoding="utf-8")
	except:
		print("#####超时错误！#####")
		out_str= whenTimeOut()
	print("小豆机器人："+out_str+"\n")