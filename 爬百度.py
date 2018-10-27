import socket
import urllib.request
import urllib.parse
import re
import json
#
header={
"Accept": "*/*",
"Accept-Encoding": "deflate, br",
"Accept-Language": "zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3",
"Cache-Control": "no-cache",
"Connection": "Keep-Alive",
"Host": "fanyi.baidu.com",
"Origin": "https://fanyi.baidu.com",
"Referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"X-Requested-With": "XMLHttpRequest"
}
while True:
	inputStr = input("输入一个字符串：")
	word=urllib.parse.quote(inputStr)
	url_api="https://fanyi.baidu.com/translate?lang=auto2zh#zh/en/%E4%BD%A0%E5%A5%BD"
	url_new=re.sub("%E4%BD%A0%E5%A5%BD",word,url_api)
	timeout=5
	socket.setdefaulttimeout(timeout)
	req = urllib.request.Request(url_new,headers=header)
	a = urllib.request.urlopen(req).read()
	main_out_str=str(a,encoding="utf-8")
	print(main_out_str)
