#Progamme 4.Wap to accept a character and perform the following.
#1.define character
#2.letter is a uppercase or lowercase
#3.numeric digit name

def character(n):
    if n >= '0' and n <= '9':
        num = int(n)
        dict = {0:'zero',1:'first',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

        print("Character is Numeric digit")
        print(dict[num])
    elif n > 'a' and  n < 'z':
        print("Character is lowercase letter")
    elif n > 'A' and n < 'Z':
        print("Character is uppercase letter")
    else:
        print("Character is special character")
n = input("enter a character")
character(n)
