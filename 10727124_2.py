#  演算法分析機測
#  學號 10727124 10727125 10727155
#  姓名 劉宇廷    石慕評    曾博暉
#  中原大學資訊工程學系
import sys
import math
import random
from fractions import Fraction

def Cal( num, n1, n2 ):
	if num == 1:
		answer = n1 + n2
	elif num == 2:
		answer = n1 - n2
	elif num == 3:
		answer = n1 * n2
	else:
		if n2 == 0:
			answer = 0
		else:
			answer = Fraction(n1, n2)
		
	return answer
	
def Sym( op ):
	if op == 1:
		sym = '+'
	elif op == 2:
		sym = '-'
	elif op == 3:
		sym = '*'
	else:
		sym = '/'
		
	return sym
	
while True == True:

	while True == True:
		c1, c2, c3, c4 = input('Input:').split()
		c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4)

		if c1 <= 13 and c2 <= 13 and c3 <= 13 and c4 <= 13:
			if c1 >= 0 and c2 >= 0 and c3 >= 0 and c4 >= 0:
				break
			else:
				print( 'Invalid input!!!\n' )
		else:
			print( 'Invalid input!!!\n' )
			
	if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0:
		print( 'BYE BYE!!!' )
		break

	
	num = [ (c1,c2,c3,c4), (c1,c2,c4,c3), (c1,c3,c2,c4), (c1,c3,c4,c2), (c1,c4,c2,c3), (c1,c4,c3,c2), 
			(c2,c1,c3,c4), (c2,c1,c4,c3), (c2,c3,c1,c4), (c2,c3,c4,c1), (c2,c4,c1,c3), (c2,c4,c3,c1), 
			(c3,c1,c2,c4), (c3,c1,c4,c2), (c3,c2,c1,c4), (c3,c2,c4,c1), (c3,c4,c1,c2), (c3,c4,c2,c1), 
			(c4,c1,c2,c3), (c4,c1,c3,c2), (c4,c2,c1,c3), (c4,c2,c3,c1), (c4,c3,c1,c2), (c4,c3,c2,c1), ]

	have = False
	speci = 0
	
	for i in range(24):
		if have == True:
			break
		for op1 in range(1, 5):
			if have == True:
				break
			for op2 in range(1, 5):
				if have == True:
					break
				for op3 in range(1, 5):
					c = Cal( op3, Cal( op2, Cal( op1, num[i][0], num[i][1]), num[i][2]), num[i][3])
					if c != 24:
						c = Cal( op2, Cal( op1, num[i][0], num[i][1]), Cal( op3, num[i][2], num[i][3] ))
						if c == 24:
							speci = 1
					if c != 24:
						c = Cal( op1, num[i][0], Cal( op2, num[i][1], Cal( op3, num[i][2], num[i][3])))
						if c == 24:
							speci = 2
						
					if c == 24:
						if speci == 1:
							print( '(', num[i][0], Sym(op1), num[i][1], ')', Sym(op2), '(', num[i][2], Sym(op3), num[i][3], ')' )
						elif speci == 2:
							print( num[i][0], Sym(op1), '(', num[i][1], Sym(op2), num[i][2], Sym(op3), num[i][3], ')' )
						elif (op1 == 1 or op1 == 2) and (op2 == 3 or op2 == 4 ):
							print( '(', num[i][0], Sym(op1), num[i][1], ')', Sym(op2), num[i][2], Sym(op3), num[i][3] )
						elif(op2 == 1 or op2 == 2) and (op3 == 3 or op3 == 4 ):
							print( '(', num[i][0], Sym(op1), num[i][1], Sym(op2), num[i][2], ')', Sym(op3), num[i][3] )
						else:
							print( num[i][0], Sym(op1), num[i][1], Sym(op2), num[i][2], Sym(op3), num[i][3] )
						
						print( 'SUCCESS!!!\n' )
						have = True
						break
	
	if have == False :
		print('No Solution!!\n')




	