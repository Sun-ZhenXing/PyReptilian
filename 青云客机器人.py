from socket import setdefaulttimeout
import urllib
from json import dumps
from re import sub
# 作者：孙振兴
# 项目地址：https://github.com/Sun-ZhenXing/PyReptilian
# 这个时候用re比较好，json应该是用regexp实现的，不如直接一点
# -----------------------------------------------------------------------------------
# 接口地址：http://api.qingyunke.com/api.php?key=free&appid=0&msg=关键词
#     key 固定参数 free
#     appid 设置为0，表示智能识别，可忽略此参数
#     msg 关键词，请参考下方参数示例，该参数可智能识别，该值请经过 urlencode 处理后再提交
# 返回结果：{"result":0,"content":"内容"}
#     result　状态，0表示正常，其它数字表示错误
#     content　信息内容 
# 温馨提示：本API完全免费使用(建议频率控制在1000次/1小时以内)
# 来自：http://api.qingyunke.com/
# -----------------------------------------------------------------------------------

while 1:
	keyWord  = input("我：")
	url_patt = urllib.parse.quote(keyWord)
	# 把中文字符转化为 URL 格式
	url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + url_patt
	setdefaulttimeout(7)
	# 设置超时
	req = urllib.request.Request(url)
	out = str(urllib.request.urlopen(req).read(),encoding="utf-8")
	outStr = sub(r"\{.+:.","",out)
	outStr = sub(r".\}","",outStr)
	# 替换掉非法字符
	# {"result":0,"content":"返回内容"}
	print(outStr)