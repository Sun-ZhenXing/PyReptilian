import requests
import re
def get_url():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'identity;q=1, *;q=0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host':'antiserver.kuwo.cn',
        'Range': 'bytes=0-',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer':base_url
    }
    url = "http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=MUSIC_"+ base_number +"&type=convert_url&response=res"
    r = s.get(url, headers=headers, allow_redirects=False)
    return r.headers['Location']
def get_aac(url):
	base_host = re.findall(r"(?:http://)(.*)", url)[0]
	base_host = base_host.split('/')[0]
	headers ={
            'Accept': '*/*',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': base_host,
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Referer':base_url,
            'Range': 'bytes=0-'
           }
	r = s.get(url, headers=headers, stream=True)
	return r
def save_aac(filename, res):
	with open(filename, 'wb') as fd:
	    for chunk in res.iter_content(chunk_size=128):
	        fd.write(chunk)
# 程序主体部分
s = requests.session()
filename = input("请输入音乐文件保存的本地路径：").strip()
base_url = input("请输入音乐播放页面url：").strip()
base_number = re.findall(r"(?:http://www.kuwo.cn/yinyue/)(\d+)(?:\?catalog=yueku2016)", base_url)[0]
