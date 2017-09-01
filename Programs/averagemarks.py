# Author: Moksh Maheshwari
#Write a program to accept roll no and marks of 3 subjects of a student, Calculate total of 3 subjects and average.

def total(m1,m2,m3):
	return(m1+m2+m3)

def average(total):
	return(total/3) 

if __name__ == '__main__':
	
	rollNo = input('Enter the roll number: ')
	subj_marks1 = int(input('Enter marks m1: '))
	subj_marks2 = int(input('Enter marks m2: '))
	subj_marks3 = int(input('Enter marks m3: '))

	x = total(subj_marks3,subj_marks2,subj_marks1)

	print('Total marks',x )
	print('Average',average(x))
