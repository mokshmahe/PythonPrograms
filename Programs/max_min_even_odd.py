# Author: Moksh Maheshwari
# Finds the Maximum, Minimum, even and odd classification. 

def findMax_Min(m,n):
	if m>n:
		print('Greater no. is: ',m)
		print('Smaller no. is: ',n)
	elif m<n:
		print('Greater no. is: ',n)
		print('Smaller no. is: ',m)
	else:
		print('The entered nos. are equal. ')

def even_odd(x):
	if x%2 == 0:
		print('The No. is even :', x)
	else:
		print('The no. is odd :',x)


if __name__ == '__main__':
	m = int(input('Enter first no.: '))
	n = int(input('Enter second no.: '))
	findMax_Min(m,n)
	even_odd(m)
	even_odd(n)