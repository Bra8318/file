#Progamme 1:Wap to find the roots of a equation.

#Equation = ax^2 + bx + c

a,b,c = eval(input("enter a,b,c "))
D = b**2 - 4*a*c
x1 = (-b + D**0.5)/ 2*a
x2 = (-b - D**0.5)/ 2*a
if D >= 0:
    print("Roots are real ",x1)
else:
     print("Roots are not real"  ,x2) 
