# Author: Moksh Maheshwari
# Function allows to split the string and join it back with '-' delimiter.
'''
Sample Input

this is a string   
Sample Output

this-is-a-string
'''
def split_and_join(line):
    s = "-"
    a = line.split(" ")
    return s.join(a)

if __name__ == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)