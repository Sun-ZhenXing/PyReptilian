import wave
from pyaudio import PyAudio,paInt16
import json
import base64
import os
import requests
import time


RATE = "16000"
FORMAT = "wav"
CUID="wate_play"
DEV_PID="1536"

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2

chunk=2014
Desktop=r"01.wav"


def save_wave_file(filename,data):
	'''save the date to the wavfile'''
	wf=wave.open(filename,'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(sampwidth)
	wf.setframerate(framerate)
	wf.writeframes(b"".join(data))
	wf.close()

def my_record(length):
	pa=PyAudio()
	stream=pa.open(format = paInt16,channels=1,
				   rate=framerate,input=True,
				   frames_per_buffer=NUM_SAMPLES)
	my_buf=[]
	count=0
	while count<TIME*length:#控制录音时间
		string_audio_data = stream.read(NUM_SAMPLES)
		my_buf.append(string_audio_data)
		count+=1
		print(count,'\t','*'*count)
	save_wave_file('01.wav',my_buf)
	stream.close()

def play():
	wf=wave.open(r"01.wav",'rb')
	p=PyAudio()
	stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
	wf.getnchannels(),rate=wf.getframerate(),output=True)
	while True:
		data=wf.readframes(chunk)
		if data=="":break
		stream.write(data)
	stream.close()
	p.terminate()

def get_token():
	server = "https://openapi.baidu.com/oauth/2.0/token?"
	grant_type = "client_credentials"
	#API Key
	client_id = "qRHV7hrxj8vtAGuZOpG0zW58"
	#Secret Key
	client_secret = "Bg3Bmx3uPeCUnvuHxnS16HLnNiVPuPnz" 

	#拼url
	url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
	#获取token
	res = requests.post(url)
	token = json.loads(res.text)["access_token"]
	return token
def get_word(token,desktop):
	with open(desktop, "rb") as f:
		speech = base64.b64encode(f.read()).decode('utf8')
	size = os.path.getsize(desktop)
	headers = { 'Content-Type' : 'application/json'} 
	url = "https://vop.baidu.com/server_api"
	data={
			"format":FORMAT,
			"rate":RATE,
			"dev_pid":DEV_PID,
			"speech":speech,
			"cuid":CUID,
			"len":size,
			"channel":1,
			"token":token,
		}

	req = requests.post(url,json.dumps(data),headers)
	result = json.loads(req.text)
	# print(result)
	ret=result["result"][0]
	return result

def MainMethod(length_input):
	if 1:
		ret = 0
		my_record(length_input)
		token=get_token()
		try:
			ret = get_word(token,Desktop)
		except:
			print("你什么也没说！")
			return ""
		# print(ret)
	return ret

if __name__ == '__main__':
	while True:
		ret = 0
		my_record(10)
		token=get_token()
		try:
			ret = get_word(token,Desktop)
		except:
			print("你什么也没说！")
		print(ret)