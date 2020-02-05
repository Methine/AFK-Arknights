# -*- coding:utf-8 -*-
#AFK scripts for Arknights
#You may need adb kits. Download it from Android Official Website. (Remember, add it to PATH, otherwise you need to put this scripts in the same folder with adb.exe)
#This scripts is also suitable for Emulator, you need to modify some of the code, DON'T forget to switch on adb mode.
#If you need to add other levels, please add it to dict according to the comment.
#IMPORTANT, EVERYTIME you need to edit input part.
#2020/2/5 Add photo contrast to avoid bug caused by network jam
#Thanks for Boar_SJTU for his prototype.

import os, time
import random
from skimage.measure import compare_ssim
from imageio import imread
import numpy as np

def imgcontrast():
	img1 = imread('org.png')
	os.popen('adb shell screencap -p /sdcard/c.png')
	os.popen('adb pull /sdcard/c.png')
	img2 = imread('c.png')
	img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
	ssim = compare_ssim(img1, img2, multichannel=True)
	return float(ssim)

#dict[level: [time(s), cost]]
dict = {'4-4': [3 * 60 + 40, 18], '1-7': [1 * 60 + 25, 6], 'CE-5': [2 * 60 + 15, 30], 'PR-D-1': [2 * 60, 18], 'PR-C-1': [1 * 60 + 37, 18], 'S3-1': [1 * 60 + 35, 15], 'S3-4': [1 * 60 + 50, 15], '4-7': [2 * 60 + 15, 18]}

#adb test
#If adb says no devices, modify and add the code below(Bluestacks)
#os.system('adb connect 127.0.0.1:5555')
os.system('adb devices')

#input part, modify it before use.
lizhi = 13
level = '1-7'

#caculation
time_cost = dict[level][0]
cost = dict[level][1]
turn = lizhi // cost 
print 'level: ' + level + ', ' + str(turn) + ' turn(s) in all'

#Pull an initial screenshot
os.popen('adb shell screencap -p /sdcard/org.png')
os.popen('adb pull /sdcard/org.png')

#loop part 
'''
#compatible for 1920x1080 resolution
for i in range(turn):
	while True:
		ssim = imgcontrast()
		print 'SSIM: ' + str(ssim)
		if ssim > 0.93:
			break
		time.sleep(5)
	os.system('adb shell input tap 1752 1011')
	time.sleep(5 + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	time.sleep(time_cost + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	print str(i + 1) + '/' + str(turn) + ' Done'
	time.sleep(5 + random.randint(0,3))
'''


#compatible for 2340x1080 resolution
for i in range(turn):
	while True:
		ssim = imgcontrast()
		print 'SSIM: ' + str(ssim)
		if ssim > 0.93:
			break
		time.sleep(5)
	os.system('adb shell input tap 2169 997')
	time.sleep(5 + random.randint(0,3))
	os.system('adb shell input tap 1872 741')
	time.sleep(time_cost + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	print str(i + 1) + '/' + str(turn) + ' Done'
	time.sleep(5 + random.randint(0,3))

#os.system('adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh')
