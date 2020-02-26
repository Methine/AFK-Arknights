# -*- coding:utf-8 -*-
#AFK scripts for Arknights
#You may need adb kits. Download it from Android Official Website. (Remember, add it to PATH, otherwise you need to put this scripts in the same folder with adb.exe)
#This scripts is also suitable for Emulator, you need to modify some of the code, DON'T forget to switch on adb mode.
#If you need to add other levels, please add it to level_dict according to the comment.
#2020/2/5 Add photo contrast to avoid bug caused by network jam.
#2020/2/6 Remove screenshot saved on sdcard.
#2020/2/6 Send QQMsg to Phone when run out of lizhi
#Thanks for Boar_SJTU for his prototype.

import os, time
import random
from skimage.measure import compare_ssim
from imageio import imread
import numpy as np
import win32gui
import win32con
import win32clipboard as w

resolution = '2340x1080'
wireless = True
#if you want to use WiFi adb, fill in your phone ip below
phone_ip = '192.168.2.103'

def xyoffset(coordinate):#coordinate[x,y]
	x = coordinate[0]
	y = coordinate[1]
	x = x + random.randint(-10,10)
	y = y + random.randint(-10,10)
	return [x,y]

class sendMsg():
	def __init__(self,receiver,msg):
		self.receiver=receiver
		self.msg=msg
		self.setText()
	#设置剪贴版内容
	def setText(self):
		w.OpenClipboard()
		w.EmptyClipboard()
		w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
		w.CloseClipboard()
	#发送消息
	def sendmsg(self):
		qq=win32gui.FindWindow(None,self.receiver)
		win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0) #win32on 见site-packages\win32\lib\win32con.py,有的博文里出现的770对用的就是win32con.WM_PASTE
		win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	
	
def imgcontrast():
	img1 = imread('org.png')
	os.popen('adb shell screencap -p /sdcard/c.png')
	os.popen('adb pull /sdcard/c.png')
	os.popen('adb shell rm /sdcard/c.png')
	img2 = imread('c.png')
	img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
	ssim = compare_ssim(img1, img2, multichannel=True)
	return float(ssim)

#level_dict[level: [time(s), cost]]
level_dict = {}
level_dict['1-7'] = [1 * 60 + 25, 6]
level_dict['3-4'] = [2 * 60 + 25, 15]
level_dict['4-2'] = [1 * 60 + 53, 18]
level_dict['4-4'] = [2 * 60 + 35, 18]
level_dict['4-7'] = [2 * 60 + 15, 18]
level_dict['4-8'] = [2 * 60 + 10, 21]
level_dict['4-9'] = [2 * 60 + 40, 21]
level_dict['6-12'] = [2 * 60, 18]
level_dict['AP-5'] = [2 * 60 + 25, 30]
level_dict['CE-5'] = [2 * 60 + 15, 30]
level_dict['PR-C-1'] = [1 * 60 + 37, 18]
level_dict['PR-D-1'] = [2 * 60, 18]
level_dict['S3-1'] = [1 * 60 + 35, 15]
level_dict['S3-4'] = [1 * 60 + 50, 15]
level_dict['S4-1'] = [2 * 60 + 10, 18]
level_dict['SA-5'] = [2 * 60 + 25, 18]

coordinate_dict = {}
coordinate_dict['1920x1080'] = [[1752, 1011], [1683, 755]]
coordinate_dict['2340x1080'] = [[2169, 997], [1872, 741]]

#WiFi ADB, you need to shell "adb tcpip 5555"(everytime you reboot your phone, you need to shell it again)
if wireless == True:
	os.system('adb connect %s' %phone_ip)
#adb test
#If adb says no devices, modify and add the code below(Bluestacks)
#os.system('adb connect 127.0.0.1:5555')
os.system('adb devices')

#use input instead
lizhi = input('Enter your Lizhi:')
while True:
	level = raw_input('Enter Level:')
	if level_dict.has_key(level):
		break
	print 'Level not included in level_dict. You may halt the script then edit it or choose another level.'

#caculation
time_cost = level_dict[level][0]
cost = level_dict[level][1]
turn = lizhi // cost 
print 'level: %s, %d turn(s) in all.' %(level, turn)

#Pull an initial screenshot
os.popen('adb shell screencap -p /sdcard/org.png')
os.popen('adb pull /sdcard/org.png')
os.popen('adb shell rm /sdcard/org.png')

#loop part 
for i in range(turn):
	while True:
		ssim = imgcontrast()
		print 'SSIM: ' + str(ssim)
		if ssim > 0.75:
			break
		time.sleep(5)
		os.system('adb shell input tap 1683 755')
	tap_coordinate = xyoffset(coordinate_dict[resolution][0])
	os.system('adb shell input tap %d %d' %(tap_coordinate[0], tap_coordinate[1]))
	time.sleep(5 + random.randint(0,3))
	tap_coordinate = xyoffset(coordinate_dict[resolution][1])
	os.system('adb shell input tap %d %d' %(tap_coordinate[0], tap_coordinate[1]))
	time.sleep(time_cost + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	print str(i + 1) + '/' + str(turn) + ' Done'
	time.sleep(5 + random.randint(0,3))

#Send QQ Msg to Phone when run out of lizhi
receiver = '我的Android手机'.decode('utf8').encode('gbk', 'ignore')
msg = '理智已经耗尽'.decode('utf8')
qq = sendMsg(receiver,msg)
qq.sendmsg()

#lock screen
os.system('adb shell input keyevent 26')
#disconnect device
#os.system('adb disconnect')

