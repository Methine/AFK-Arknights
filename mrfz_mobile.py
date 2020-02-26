# -*- coding:utf-8 -*-
#With Termux, you can use this script.
import os, time
import random

resolution = '2340x1080'

def xyoffset(coordinate):#coordinate[x,y]
	x = coordinate[0]
	y = coordinate[1]
	x = x + random.randint(-10,10)
	y = y + random.randint(-10,10)
	return [x,y]

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

#adb test
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

#wait for 15s
print 'Now you have 15s, switch back to mrfz game.'
time.sleep(15)

#loop part 
for i in range(turn):
	tap_coordinate = xyoffset(coordinate_dict[resolution][0])
	os.system('adb shell input tap %d %d' %(tap_coordinate[0], tap_coordinate[1]))
	time.sleep(5 + random.randint(0,3))
	tap_coordinate = xyoffset(coordinate_dict[resolution][1])
	os.system('adb shell input tap %d %d' %(tap_coordinate[0], tap_coordinate[1]))
	time.sleep(time_cost + random.randint(0,3))
	os.system('adb shell input tap 1683 755')
	print str(i + 1) + '/' + str(turn) + ' Done'
	time.sleep(5 + random.randint(0,3))

#lock screen
os.system('adb shell input keyevent 26')
#disconnect device
os.system('adb disconnect')
