def roots(a,b,c):
	x = b**2 - 4*a*c

	if (x == 0):
		print('The roots are: {} and {}'.format((-b/2*a),(-b/2*a)))
	elif (x > 0):
		print('The roots are: {} and {}'.format(((-b + x**0.5) / 2*a ),((-b - x**0.5) / 2*a )))
	else:
		print('The roots are imaginary: {} and {}'.format(((-b/2*a + x**0.5 / 2*a)),(-b/2*a - x**0.5 / 2*a)))


if __name__ == '__main__':
	print('Enter the values a,b,c for calculations.\n Equation is of the form ax^2 + bx + c = 0')
	a = int(input('a'))
	b = int(input('b'))
	c = int(input('c'))

	roots(a,b,c)