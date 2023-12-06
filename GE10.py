# write a function that prints a dictionary of keys 1 to 5 and value are cube of keys.
n = eval(input("enter number"))
def cube():
    dict = {}
    for num in range(1,n):
     
      cube = num ** 3
      dict[num] = cube
    return dict

print(cube())
