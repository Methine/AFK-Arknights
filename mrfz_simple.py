# -*- coding:utf-8 -*-
#AFK scripts for Arknights
#You may need adb kits. Download it from Android Official Website. (Remember, add it to PATH, otherwise you need to put this scripts in the same folder with adb.exe)
#This scripts is also suitable for Emulator, you need to modify some of the code, DON'T forget to switch on adb mode.
#If you need to add other levels, please add it to dict according to the comment.
#IMPORTANT, EVERYTIME you need to edit input part.
#Thanks for Boar_SJTU for his prototype.
#Remove all impractical function.
#2020/2/7 Now you can use WiFi ADB
import os, time
import random

#dict[level: [time(s), cost]]
dict = {}
dict['1-7'] = [1 * 60 + 25, 6]
dict['3-4'] = [2* 60 + 25, 15]
dict['4-4'] = [2 * 60 + 35, 18]
dict['4-7'] = [2 * 60 + 15, 18]
dict['4-8'] = [2 * 60 + 10, 21]
dict['4-9'] = [2 * 60 + 40, 21]
dict['AP-5'] = [2 * 60 + 25, 30]
dict['CE-5'] = [2 * 60 + 15, 30]
dict['PR-C-1'] = [1 * 60 + 37, 18]
dict['PR-D-1'] = [2 * 60, 18]
dict['S3-1'] = [1 * 60 + 35, 15]
dict['S3-4'] = [1 * 60 + 50, 15]

#adb test
#If adb says no devices, modify and add the code below(Bluestacks)
#os.system('adb connect 127.0.0.1:5555')
#os.system('adb devices')

#WiFi ADB, you need to shell "adb tcpip 5555"(everytime you reboot your phone, you need to shell it again)
os.system('adb connect 192.168.2.103')

#use input instead
lizhi = input('Enter your Lizhi:')
while True:
	level = raw_input('Enter Level:')
	if dict.has_key(level):
		break
	print 'Level not included in dict. You may halt the script then edit it or choose another level.'

#caculation
time_cost = dict[level][0]
cost = dict[level][1]
turn = lizhi // cost 
print 'level: ' + level + ', ' + str(turn) + ' turn(s) in all'

#loop part 
'''
#compatible for 1920x1080 resolution
for i in range(turn):
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
	os.system('adb shell input tap 2169 997')
	time.sleep(5 + random.randint(0,3))
	os.system('adb shell input tap 1872 741')
	time.sleep(time_cost + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	print str(i + 1) + '/' + str(turn) + ' Done'
	time.sleep(5 + random.randint(0,3))

#lock screen
os.system('adb shell input keyevent 26')
#disconnect device
os.system('adb disconnect')
