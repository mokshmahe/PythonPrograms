def pattern1(lvl):
	'''pattern 1:
	*
	**
	***
	****
	''' 
	for i in range(1,lvl+1):
		print('')
		for j in range(i):
			print('*',end ='')


def pattern2(lvl):
	'''pattern2
	   *
	  **
	 ***
	****
	'''
	space = lvl
	for i in range(lvl+1):
		print(' '*space+'*'*i)
		space-= 1

def pattern3(lvl):
	'''pattern3
	   *
	  ***
	 *****
	*******
	'''
	space = lvl-1
	for i in range(1,lvl+1):
		print(' '*space + '*'*(2*i-1))
		space-=1



if __name__ == '__main__':
	lvl = int(input('Enter the no. of levels:'))
	pattern1(lvl)
	print()
	pattern2(lvl)
	print()
	pattern3(lvl)
	print()
	