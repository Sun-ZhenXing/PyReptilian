from requests import post,get
from json import loads
from os import system
headers = {
	'Host': 'c.y.qq.com',
	'Referer': 'http://c.y.qq.com/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
				  'Safari/537.36 '
}
def find_song(word):
	"""
	查找歌曲
	:param word: 歌曲名
	:return: 返回歌曲mid
	"""
	get_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n' \
			  '=20&w=' + word
	res1 = get(get_url, headers=headers)
	get_json = loads(res1.text.strip('callback()[]'))
	jsons = get_json['data']['song']['list']
	songmid = []
	media_mid = []
	song_singer = []
	i = 1
	s0 = ""
	for song in jsons:
		# print(i, ':' + song['songname'], '---', song['singer'][0]['name'], song['songmid'], song['media_mid'])
		s0 = s0+str(i)+':'+ str(song['songname'])+'-'+str(song['singer'][0]['name']+"\n")
		songmid.append(song['songmid'])
		#media_mid.append(song['media_mid'])
		song_singer.append(song['singer'][0]['name'])
		i = i + 1
	return songmid, song_singer,s0
def douqq_post(mid):
	"""
	返回歌曲下载url
	:param mid:歌曲mid
	:return: 字典
	"""
	post_url = 'http://www.douqq.com/qqmusic/qqapi.php'
	data = {'mid': mid}
	res = post(post_url, data=data)
	get_json = loads(res.text)
	return eval(get_json)

while __name__ == '__main__':
	if 1:
		q="mp3_h"
		songname = input("输入下载的歌曲名:")
		song_mid, singer,count = find_song(songname)
		print(count)
		i=1
		for x in song_mid:
			s0=str(i)+"："+str(douqq_post(x)[q])+"\n"
			s0=s0.replace('\/\/', '//').replace('\/', '/')
			i+=1
			print(s0)
		#dic = douqq_post(song_mid)
		#postfix, url = choice_download(dic)
		#print(url)
		#save_path = "D:\\"
		#download_file(url, save_path + songname + ' - ' + singer + postfix)
		#print('如果这首歌在库存中，那么下载已经完成了。请检查文件的大小。')
		#system("explorer "+save_path)
