#!C:\Users\PC\AppData\Local\Programs\Python\Python36-32\python.exe
# See http://cens.ioc.ee/projects/f2py2e/
from qqbot import QQBotSlot as qqbotslot,RunBot 
import socket
import urllib.request
import urllib.parse
import re
# 加载相关模块
print("##########模块加载成功！##########")
# 全局变量
global membTrueSet
global membCannot
membTrueSet=set()
# 创建好友集合
membCannot=set()
# 不会响应的好友集合
helpSTR="""群聊天系统使用说明：



"""
# 小i机器人函数
def xiaoi(inputStr):
	try :
		word=urllib.parse.quote(inputStr)
		# 更新网址：
		url_api="http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22f5b61eba68144a429b543a0d9a98eb90%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%22873a71883fd74449b3c99874cf7ad886%22%2C%22body%22%3A%7B%22content%22%3A%22%E4%BD%A0%E5%A5%BD%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1534051772519"
		# %E4%BD%A0%E5%A5%BD
		url_new=re.sub("%E4%BD%A0%E5%A5%BD",word,url_api)
		timeout=5
		socket.setdefaulttimeout(timeout)
		req = urllib.request.Request(url_new)
		a = urllib.request.urlopen(req).read()
		main_out_str=str(a,encoding="utf-8")
		# 格式化json为文字
		main_out_str=format_func(main_out_str)
		# 检测是否是正确回答
		boolX = check_back_str(main_out_str)
			if boolX==False:
				return False
	except:
		print("##########超时错误##########")
		return False
	return(main_out_str)
# 检测小i机器人是否听懂了
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
		print("#####小i没听明白！#####")
		return False
	else:
		return True
# 格式化字符串，防止出现HTML字符
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
# 出现超时错误的时候，检测回答并选择回复
def whenTimeOut():
	if((re.search("你好|在吗|在干什么|hello|Hello|Hi|hi",main_str))):
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
# 当找不到回答的时候运行，获取随机的回答
def getRandomPage():
	#当小豆无话可说时执行
	URLmain="http://api.douqq.com/?key=MlVZZjR3N0ZqVj1ISXBZTG1RVDBMMEI9VEJjQUFBPT0&msg=%E4%B8%80%E8%A8%80"
	timeout = 5
	socket.setdefaulttimeout(timeout)
	req = urllib.request.Request(URLmain)
	a = urllib.request.urlopen(req).read()
	out_str=str(a,encoding="utf-8")
	return out_str
# 小豆机器人函数
def xiaodou(inputStr):
	try:
		word=urllib.parse.quote(main_str)
		url_api="http://api.douqq.com/?key=MlVZZjR3N0ZqVj1ISXBZTG1RVDBMMEI9VEJjQUFBPT0&msg="+word
		timeout = 5
		socket.setdefaulttimeout(timeout)
		req = urllib.request.Request(url_api)
		a = urllib.request.urlopen(req).read()
		if(re.search("<head><title>",str(a,encoding="utf-8"))):
			# 页面不存在
			out_str=whenTimeOut()
		else:
			out_str=str(a,encoding="utf-8")
	except:
		print("#####超时错误！#####")
		out_str= whenTimeOut()
	return out_str
# ------------------------------主程序------------------------------
@qqbotslot
def onQQMessage(bot,contact,member,content):
	global membTrueSet
	global membCannot
	# 主函数，有人发信息给我执行
	if(member):
		# 如果是群聊就不回话
		print("【系统提示】————群聊天————")
	else:
		# 裁剪类型好友为字符串
		friend=str(contact)
		friend=friend[3:]
		friend=friend[:-1]
		if content=="Delete Data":
			# 撤销删除指令
			bot.SendTo(contact,"感谢你再次选择我，我不会再离开了！")
			if(friend in membCannot):
				membCannot=membCannot-{friend}
		if(friend in membCannot):
			# 屏蔽的联系人不回
			print("【系统提示】————屏蔽联系人发来消息————")
		else:
			if(friend in membTrueSet):
				# 判断是否已经打过招呼
				if content=="":
					# 发送图片或其他
					bot.SendTo(contact,friend+"，你别只发图片啊，我现在看不懂，咱聊点别的？")
				elif content=="帮助":
					# 使用帮助
					bot.SendTo(contact,helpSTR)
				elif content=="住口":
					# 将好友列入闭嘴的集合
					bot.SendTo(contact,"小豆机器人不会再说话了，输入：Delete Data 解除")
					membCannot={friend}|membCannot
				elif content=="关于":
					# 显示关于内容
					bot.SendTo(contact,"智能聊天机器人：版本v2.0\n作者：孙振兴(东海高级中学树人高二2班)\n说明：程序由python脚本语言编写，使用或有任何意见请联系作者QQ1006925066")
				elif content==" " or content =="  ":
					# 好友什么也没说
					bot.SendTo(contact,"我让你发空格！")
				else:
					# 没有使用指令，聊天，查找聊天代理服务器并返回内容
					out_str=xiaoi(content)
					if out_str==False:
						# 小i回答失败，启动API 小豆
						out_str=xiaodou(content)
					# 发送得到的页面
					bot.SendTo(contact,out_str)
			else:
				# 没打过就打招呼，加入到集合中
				bot.SendTo(contact,friend+"，你好，我是AI机器人小胖\n获取更多信息输入：帮助\n不想我说话输入：住口\n关于程序信息输入：关于\n聊的开心！")
				newSet={"孙振兴",friend}
				membTrueSet=membTrueSet|newSet
# 开始运行
RunBot()