#Programme 5.Wap to perform the following operations on a string.

#find the frequency of a character in a string.
def frequency():
    character = input("enter character")
    freq = 0
    for i in string:
        if i == character:
            freq += 1
    print("frequency of ",character,"is",freq)
string = "hello python"
frequency()


#Replace a character by another character in a string.
string = "hello python"
str2 = string.replace("h","w")
print(str2)

#Remove the first occurence of a character in a string.
string = "hello python"
str2 = string[1:len(string)]
print(str2)

#Remove the all occurence of a character in a string.
string = "hello python"
str2 = string[:0]
print(str2,None)


