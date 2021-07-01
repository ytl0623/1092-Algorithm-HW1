#  演算法分析機測
#  學號 10727124 10727125 10727155
#  姓名 劉宇廷    石慕評    曾博暉
#  中原大學資訊工程學系
import sys
import math
import random

def Gcd( a, b ):
	if b == 0:
		return a
	else:
		return Gcd( b, a%b )

def Cal( b1, b2 ):
	step1, step2 = b1, b2
	x,y = 1, 1
	while True == True:
		
		if b1 != b2:
			if (tar%(b1 - b2)) == 0:
				base = tar/(b1 - b2)
				x = x*base
				y = y*-base 
				break

		if ( b1 <= b2 ):
			b1 = b1 + step1
			x = x + 1
		else:
			b2 = b2 + step2
			y = y + 1
	
	return x, y
	
def PrintPrcs( b1, b2, x, y ):
	curb1, curb2 = 0, 0
	totalb1 = b1*x
	totalb2 = b2*y
	while x != 0 and y != 0:
		if x > 0:
			print('Fill A')
			curb1 = b1
			x = x - 1
		elif y > 0:
			print('Fill B')
			curb2 = b2
			y = y - 1
		
		while True == True:
			if x < 0:
				print('Pour B A')
				if (b1-curb1) > curb2:
					totalb1 = totalb1 + b2
					curb1 = curb1 + b2
					curb2 = 0
				elif (b1-curb1) < curb2:
					totalb1 = totalb1 + (b1-curb1)
					curb2 = curb2 - (b1-curb1)
					curb1 = b1
				
				if totalb1 == 0:
					x = 0
					break				
				
				if curb1 == b1:
					print('Empty A')
					curb1 = 0
					x = x + 1
				
				if curb2 == 0:
					break
				
			elif y < 0:
				print('Pour A B')
				if (b2-curb2) > curb1:
					totalb2 = totalb2 + b1
					curb2 = curb2 + b1
					curb1 = 0
				elif (b2-curb2) < curb1:
					totalb2 = totalb2 + (b2-curb2)
					curb1 = curb1 - (b2-curb2)
					curb2 = b2	

				if curb2 == b2:
					print('Empty B')	
					curb2 = 0
					y = y + 1

				if curb1 == 0:
					break		
					
			if x == 0 and y == 0:
				if curb2 == 0:
					print('Pour A B')
				break

	
while True == True:

	while True == True:
		b1, b2, tar = input('Input:').split()
		b1, b2, tar = int(b1), int(b2), int(tar)
		d = Gcd( b1, b2 )
		print
		if tar%d != 0 or tar > b2:
			print('No Answer!!!\n')
		elif b1 < 0 or b2 < 0 or tar < 0:
			print('Invalid input\n')
		elif b1 >= 0 and b2 >= 0 and tar >= 0:
			break
			
	if b1 == 0 and b2 == 0 and tar == 0:
		break
	
	x, y = Cal(b1, b2)
	print(x, y)
	PrintPrcs( b1, b2, x, y )
	print('\nSUCCESS!!!\n')