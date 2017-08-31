#You have been given a String S consisting of uppercase and lowercase English alphabets.
#You need to change the case of each alphabet in this String.
#That is, all the uppercase letters should be converted to lowercase and all the lowercase 
#letters should be converted to uppercase. You need to then print the resultant String to output.

#Code:
S = input()	#Takes input string
ans = ''
for i in S:
	#checks whether the element of the string is in lower case or not, if it is in lower case 
	#then change it to upper case and vice-versa.
    if i.islower():		
       ans+=i.upper()
    else:
       ans+=i.lower()
print(ans)
        