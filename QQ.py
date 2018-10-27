from qqbot import QQBotSlot as qqbotslot,RunBot 
from socket import setdefaulttimeout
from re import sub
from urllib import request
from json import dumps

global membTrueSet
global membCannot
membTrueSet=set()
# 创建同学集合
membCannot=set()
# 不会响应的好友集合
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
					"city": "连云港",
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
	timeout = 2
	setdefaulttimeout(timeout)
	req = request.Request(url_api,data=dumps(data0).encode("utf-8"))
	req.add_header('Content-Type','application/json')
	response=request.urlopen(req)
	outjson=str(response.read(),encoding="utf-8")
	print("[INFO]\n",outjson+"\n[/INFO]")
	out_str=sub(r".+value","",outjson)
	out_str=sub(r'"}}]}',"",out_str)
	out_str=out_str[12:] 
	return out_str
@qqbotslot
def onQQMessage(bot,contact,member,content):
	global membTrueSet
	global membCannot
	helpSTR="""智能机器人帮助：
	查询输入：什么是+内容
	计算如13+2-5
	聊天现在支持情感分析啦！更多功能欢迎提供意见，后续可能增加下载歌曲、在线查询、新闻和推荐功能。
	2018年8月30日更新，孙振兴设计。代码开源，学习请联系作者。
	"""
	# 主函数，有人发信息给我执行
	if(member):
		# 如果是群聊就不回话
		pass
	else:
		friend=str(contact)
		friend=friend[3:]
		friend=friend[:-1]
		if content=="解除禁言":
			# 撤销删除指令
			bot.SendTo(contact,"感谢你再次选择我！")
			if(friend in membCannot):
				membCannot=membCannot-{friend}
		if(friend in membCannot):
			# 屏蔽的联系人不回
			pass
		else:
			if(friend in membTrueSet):
				# 判断是否已经打过招呼
				if content=="帮助":
					# 使用帮助
					bot.SendTo(contact,helpSTR)
				elif content=="不许说话":
					# 将好友列入闭嘴集合
					bot.SendTo(contact,"我不会再说话了\n输入：解除禁言 可以解除哦！")
					membCannot={friend}|membCannot
				else:
					# 没有使用指令，聊天
					try:
						out_str=sendMessage(content)
					except:
						out_str="请求错误。"
					bot.SendTo(contact,out_str)
			else:
				# 没打过就打招呼，加入到集合中
				bot.SendTo(contact,friend+"，你好，智能机器人图灵\n和伟大的计算机之父阿兰·图灵同名哦！\n获取更多信息输入：帮助\n不想我说话输入：不许说话")
				newSet={" ",friend}
				membTrueSet=membTrueSet|newSet

RunBot()
