# Author: Moksh Maheshwari
#Swaps the value of two variables.

def swap(a,b):
	temp = a
	a=b
	b=temp
	return (a,b)

if __name__ == '__main__':
	a=int(input())
	b=int(input())
	c = list(swap(a,b))
	print(c , type(c))
