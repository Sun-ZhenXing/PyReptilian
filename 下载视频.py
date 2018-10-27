from os import system
while 1:
    video=input("输入视频的URL地址！\n")
    print("现在开始下载！")
    system("lulu "+video)
    print("下载完成！")
