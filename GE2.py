#Programme 2:WAp to accept a number n.

print("1.Number is prime")
print("2.All prime number till n")
print("3.First n prime number")
def prime_number(n):
    if n >= 2:
        for i in range(2,n):
            if n % i == 0:
                print("Not a prime number ",n)
                break
        else:
            print("prime number",n)
    else:
        print("number is less than 2")

def all_prime_number(n):
    for num in range (1,n):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num,end = ',')

def till_n_prime_number(n):
    count = 0
    number = 2
    while count < n:
        for i in range(2,number):
            if number % i == 0:
                number += 1
                break
        else:
            print(number ,end = ',')
            number += 1
            count += 1
            
n = eval(input("enter number"))
choice = int(input("enter choice"))
if choice == 1:
    print(prime_number(n))
elif choice == 2:
    print(all_prime_number(n))
elif choice == 3:
    print(till_n_prime_number(n))
else:
    print("none")

        
    
    
    
    

