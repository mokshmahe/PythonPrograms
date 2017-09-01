# Author: Moksh Maheshwari

#lists are mutable (they can be changed), and tuples are immutable (they cannot be changed)


#By Slicing The string and joining it back.
def mutate_string_method1(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string


# By converting the string to list and then change the value.
def mutate_string_method2(string, position, character):
    s = ""
    l = list(string)
    l[position] = character
    string = s.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string_method1(s, int(i), c)
    print("By Method 1:", s_new)
    s_new = mutate_string_method2(s, int(i), c)
    print("By Method 2:",s_new)