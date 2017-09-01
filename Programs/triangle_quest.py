# Author: Moksh Maheshwari
'''You are given a positive integer . Print a numerical triangle of height  like the one below:

1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines.

Sample Input

5
Sample Output

1
22
333
4444
'''

#code:
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*(10**i -1)//9)