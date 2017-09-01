# Author: Moksh Maheshwari

#To calculate LCM of two numbers:

def LCM(x,y):
	max_n = max(x,y)
	k = max_n

	while True:
		if (k%x == 0 and k%y ==0):
			lcm = k
			break
		k+=max_n
	return lcm


# To calculate HCF of two numbers:
def HCF(x,y):
	min_n = min(x,y)

	for i in range(1, min_n + 1):
		if(x%i ==0 and y%i == 0):
			hcf = i
	return hcf



if __name__ == '__main__':
	x = int(input('Enter the first no.:'))	
	y = int(input('Enter the second no.:'))

	print('LCM and HCF of {} and {} are {} and {} respectively.'.format(x,y,LCM(x,y),HCF(x,y)))