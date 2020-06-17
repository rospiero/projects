# a small caesar code reviewed
#library import
import random

# the function going to work on the caeser coder
def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
text = print("*********Please input the text to cypher: *********")
text=str(input())


print("please input the key to use for the cypher")
s=int(input())

#this is the control check statement:
#print (text,s)
print(encrypt(text,s))
