#Wap to swap the first n character of two strings.

str1 = "hello python"
str2 = "welcome in java"
n = eval(input("enter swap character no."))
s = str1[0:n]
p = str2[0:n]
if n < min(len(str1),len(str2)):   
   print(str1.replace(s,p))
else:
    print(str2.replace(s,p))
