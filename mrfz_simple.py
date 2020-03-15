# -*- coding:utf-8 -*-
#AFK scripts for Arknights
#You may need adb kits. Download it from Android Official Website. (Remember, add it to PATH, otherwise you need to put this scripts in the same folder with adb.exe)
#This scripts is also suitable for Emulator, you need to modify some of the code, DON'T forget to switch on adb mode.
#If you need to add other levels, please add it to dict according to the comment.
#Thanks for Boar_SJTU for his prototype.
#Remove all impractical function.
#2020/2/7 Now you can use WiFi ADB
import os, time
import random

resolution = '2340x1080'
wireless = 	True
#if you want to use WiFi adb, fill in your phone ip below
phone_ip = '192.168.2.103'

def xyoffset(coordinate):#coordinate[x,y]
	x = coordinate[0]
	y = coordinate[1]
	x = x + random.randint(-10,10)
	y = y + random.randint(-10,10)
	return [x,y]

def tap(tap_coordinate):
	os.system('adb shell input tap %d %d' %(tap_coordinate[0], tap_coordinate[1]))
	return 0
	
#dict[level: [time(s), cost]]
level_dict = {}
level_dict['1-7'] = [1 * 60 + 25, 6]
level_dict['3-4'] = [2 * 60 + 25, 15]
level_dict['4-2'] = [1 * 60 + 53, 18]
level_dict['4-4'] = [2 * 60 + 35, 18]
level_dict['4-5'] = [2 * 60 + 10, 18]
level_dict['4-7'] = [2 * 60 + 15, 18]
level_dict['4-8'] = [2 * 60 + 10, 21]
level_dict['4-9'] = [2 * 60 + 40, 21]
level_dict['4-10'] = [2 * 60 + 35, 21]
level_dict['6-11'] = [2 * 60 + 50, 21]
level_dict['6-12'] = [2 * 60, 18]
level_dict['AP-5'] = [2 * 60 + 25, 30]
level_dict['CA-5'] = [2 * 60 + 5, 30]
level_dict['CE-5'] = [2 * 60 + 15, 30]
level_dict['LS-5'] = [2 * 60 + 20, 30]
level_dict['PR-A-2'] = [2 * 60 + 30, 36]
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
	print 'Level not included in dict. You may halt the script then edit it or choose another level.'

#caculation
time_cost = level_dict[level][0]
cost = level_dict[level][1]
turn = lizhi // cost 
print 'level: %s, %d turn(s) in all.' %(level, turn)

#loop part 
for i in range(turn):
	tap_coordinate = xyoffset(coordinate_dict[resolution][0])
	tap(tap_coordinate)
	time.sleep(5 + random.randint(0,3))
	tap_coordinate = xyoffset(coordinate_dict[resolution][1])
	tap(tap_coordinate)
	time.sleep(time_cost + random.randint(0,3))
	tap([1683,755])
	print '%d/%d Done'%(i + 1,turn)
	time.sleep(5 + random.randint(0,3))

#lock screen
os.system('adb shell input keyevent 26')
#disconnect device
os.system('adb disconnect')
