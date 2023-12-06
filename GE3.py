#Programme 3.Wap to creat a pyramid of the character '*' and a reverse pyramid.
n = eval(input("enter line of pyramid"))
for i in range(n):
    for j in range(i,n):
        print(' ',end = ' ')
    for j in range(i):
        print("*",end = ' ' )
    for j in range (i+1):
        print("*",end = ' ' )
    print()
        
for i in range (n):
    for j in range(i+2):
        print(" " ,end = ' ')
    for j in range(i,n-1):
       print("*",end = ' ')
    for j in range(i,n-2):
        print("*",end= ' ')
    print()
    
