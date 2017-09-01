def split_and_join(line):
    # write your code here
    s = "-"
    a = line.split(" ")
    return s.join(a)

if __name__ == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)