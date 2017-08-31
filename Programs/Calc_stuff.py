def Add(a,b):
	return a+b

def Sub(a,b):
	return a-b

def Mul(a,b):
	return a*b

def Div(a,b):
	return a/b

def x_raiseto_y(a,b):
	return a**b

def simpleInterest(p,r,t):
	return p*r*t/100

if __name__ == '__main__':
	a = int(input('Enter a for calculations: '))
	b = int(input('Enter b for calculations: '))
	p = int(input('Enter p for calculations: '))
	r = int(input('Enter r for calculations: '))
	t = int(input('Enter t for calculations: '))

	print("Addition of two numbers is: ",Add(a,b))
	print("Subtraction of two numbers is: ",Sub(a,b))
	print("Multplication of two numbers is: ",Mul(a,b))
	print("Division of two numbers is: ",Div(a,b))
	print("x_raiseto_y of two numbers is: ",x_raiseto_y(a,b))
	print("SI is: ",simpleInterest(p,r,t))
