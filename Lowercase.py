# Python Program to Convert String to Lowercase using ASCII Values

string = input("Please Enter your String : ")
string1 = ''

for i in string:
    if (ord(i) >= 65 and ord(i) <= 90):
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i

print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)

